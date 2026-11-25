"""Clean a messy invoice CSV into a live-formula Excel workbook with native conditional formatting.

Mirrors the Claude Sheets invoice demo (18 rows, 6 planted issues) deterministically in Python:
- Removes duplicate Invoice_ID rows (logged to Please_Check)
- Normalizes amounts, dates, and vendor casing/whitespace
- Infers missing categories from vendor history (flagged in Please_Check for human review)
- Builds Invoices tab with live Excel formulas + native FormulaRule conditional formatting
- Builds Summary tab with live budget/overdue/vendor SUMIF formulas + a reconciliation Check cell
"""

from __future__ import annotations

import csv
from datetime import date, datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
INPUT_CSV = HERE / "messy_invoices_sample.csv"
OUTPUT_XLSX = HERE / "clean_invoices.xlsx"

BUDGET_USD = 42_000.00
AS_OF_DATE = date(2026, 11, 24)


def parse_amount(raw: str) -> float:
    cleaned = raw.strip().replace("$", "").replace(",", "")
    return float(cleaned)


def parse_date(raw: str) -> date:
    text = raw.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {raw!r}")


def load_and_clean(csv_path: Path) -> tuple[list[dict], list[dict]]:
    """Return (cleaned_rows, review_items)."""
    with csv_path.open(newline="", encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    # Build canonical vendor capitalization map from cleanly cased names
    canonical_vendors: dict[str, str] = {}
    for row in raw_rows:
        raw_v = row["Vendor"].strip()
        key = raw_v.lower()
        # Prefer names that already have uppercase letters (e.g. PixelCraft Studio)
        if key not in canonical_vendors or (
            any(c.isupper() for c in raw_v) and not any(c.isupper() for c in canonical_vendors[key])
        ):
            canonical_vendors[key] = raw_v

    seen_ids: set[str] = set()
    cleaned: list[dict] = []
    review_items: list[dict] = []

    for idx, row in enumerate(raw_rows, start=2):
        inv_id = row["Invoice_ID"].strip()
        if inv_id in seen_ids:
            review_items.append(
                {
                    "Severity": "Info (Auto-fixed)",
                    "Invoice_ID": inv_id,
                    "Issue": "Duplicate invoice row removed",
                    "Action_Taken": f"Dropped duplicate at source CSV row {idx}",
                }
            )
            continue
        seen_ids.add(inv_id)

        raw_vendor = row["Vendor"]
        std_vendor = canonical_vendors[raw_vendor.strip().lower()]
        if raw_vendor != std_vendor:
            review_items.append(
                {
                    "Severity": "Info (Auto-fixed)",
                    "Invoice_ID": inv_id,
                    "Issue": f"Non-standard vendor name ({raw_vendor!r})",
                    "Action_Taken": f"Standardized to {std_vendor!r}",
                }
            )

        cleaned.append(
            {
                "Invoice_ID": inv_id,
                "Vendor": std_vendor,
                "Category": row["Category"].strip(),
                "Amount": parse_amount(row["Amount"]),
                "Due_Date": parse_date(row["Due_Date"]),
                "Status": row["Status"].strip().title(),
                "Notes": row["Notes"].strip(),
            }
        )

    # Infer blank categories from the same vendor's existing invoices, and ALWAYS flag for human review
    vendor_categories: dict[str, set[str]] = {}
    for r in cleaned:
        if r["Category"]:
            vendor_categories.setdefault(r["Vendor"], set()).add(r["Category"])

    for r in cleaned:
        if not r["Category"]:
            candidates = sorted(vendor_categories.get(r["Vendor"], set()))
            guess = candidates[0] if len(candidates) == 1 else "UNCATEGORIZED"
            r["Category"] = guess
            review_items.insert(
                0,
                {
                    "Severity": "PLEASE CHECK",
                    "Invoice_ID": r["Invoice_ID"],
                    "Issue": "Blank category in source CSV",
                    "Action_Taken": (
                        f"Inferred {guess!r} from vendor {r['Vendor']!r} history "
                        f"and note ({r['Notes']!r}). Confirm before sharing."
                    ),
                },
            )

    return cleaned, review_items


def build_workbook(rows: list[dict], review_items: list[dict], out_path: Path) -> None:
    wb = Workbook()

    # Shared styles
    header_fill = PatternFill("solid", fgColor="1F2937")
    header_font = Font(color="FFFFFF", bold=True, name="Calibri", size=11)
    bold_font = Font(bold=True, name="Calibri", size=11)
    title_font = Font(bold=True, name="Calibri", size=14, color="111827")
    section_font = Font(bold=True, name="Calibri", size=11, color="1F2937")
    body_font = Font(name="Calibri", size=11)
    thin_border = Border(bottom=Side(style="thin", color="E5E7EB"))

    # Conditional formatting styles
    overdue_fill = PatternFill("solid", fgColor="FFC7CE")
    overdue_font = Font(color="9C0006", bold=True, name="Calibri", size=11)
    ok_fill = PatternFill("solid", fgColor="C6EFCE")
    ok_font = Font(color="006100", bold=True, name="Calibri", size=11)
    warn_fill = PatternFill("solid", fgColor="FFEB9C")
    warn_font = Font(color="9C6500", bold=True, name="Calibri", size=11)

    # ------------------------------------------------------------------
    # Sheet 1: Invoices
    # ------------------------------------------------------------------
    ws_inv = wb.active
    ws_inv.title = "Invoices"

    headers = [
        "Invoice_ID",
        "Vendor",
        "Category",
        "Amount",
        "Due_Date",
        "Status",
        "Notes",
        "Overdue_Flag",
        "Days_Overdue",
    ]
    ws_inv.append(headers)
    for col_idx in range(1, len(headers) + 1):
        cell = ws_inv.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="left", vertical="center")

    for row_idx, r in enumerate(rows, start=2):
        # Live Excel formulas referencing Summary!$B$3 (As-Of Date)
        overdue_formula = f'=IF(AND(F{row_idx}="Unpaid",E{row_idx}<Summary!$B$3),"YES","NO")'
        days_formula = f'=IF(H{row_idx}="YES",Summary!$B$3-E{row_idx},0)'

        ws_inv.append(
            [
                r["Invoice_ID"],
                r["Vendor"],
                r["Category"],
                r["Amount"],
                r["Due_Date"],
                r["Status"],
                r["Notes"],
                overdue_formula,
                days_formula,
            ]
        )
        for col_idx in range(1, len(headers) + 1):
            c = ws_inv.cell(row=row_idx, column=col_idx)
            c.font = body_font
            c.border = thin_border

        ws_inv.cell(row=row_idx, column=4).number_format = "$#,##0.00"
        ws_inv.cell(row=row_idx, column=5).number_format = "yyyy-mm-dd"
        ws_inv.cell(row=row_idx, column=8).alignment = Alignment(horizontal="center")
        ws_inv.cell(row=row_idx, column=9).number_format = "0"

    last_inv_row = len(rows) + 1
    ws_inv.freeze_panes = "A2"
    ws_inv.auto_filter.ref = f"A1:I{last_inv_row}"

    # NATIVE EXCEL CONDITIONAL FORMATTING:
    # Highlights the entire row A..I red whenever column H (Overdue_Flag) evaluates to "YES".
    # Try changing any overdue row's Status in column F from "Unpaid" to "Paid" in Excel/Sheets!
    ws_inv.conditional_formatting.add(
        f"A2:I{last_inv_row}",
        FormulaRule(formula=['$H2="YES"'], fill=overdue_fill, font=overdue_font),
    )

    # ------------------------------------------------------------------
    # Sheet 2: Summary (all live formulas)
    # ------------------------------------------------------------------
    ws_sum = wb.create_sheet("Summary")
    ws_sum["A1"] = "Q4 Marketing Invoices — Live Budget Summary"
    ws_sum["A1"].font = title_font

    ws_sum["A2"] = "Budget"
    ws_sum["B2"] = BUDGET_USD
    ws_sum["B2"].number_format = "$#,##0.00"
    ws_sum["C2"] = "Edit to recalculate remaining budget"

    ws_sum["A3"] = "As-Of Date"
    ws_sum["B3"] = AS_OF_DATE
    ws_sum["B3"].number_format = "yyyy-mm-dd"
    ws_sum["C3"] = "Replace with =TODAY() for daily auto-updates"

    metrics = [
        ("Total Spend (Cleaned)", f"=SUM(Invoices!D2:D{last_inv_row})", "$#,##0.00"),
        ("Paid", f'=SUMIF(Invoices!F2:F{last_inv_row},"Paid",Invoices!D2:D{last_inv_row})', "$#,##0.00"),
        ("Unpaid", f'=SUMIF(Invoices!F2:F{last_inv_row},"Unpaid",Invoices!D2:D{last_inv_row})', "$#,##0.00"),
        ("Budget Remaining", "=B2-B5", "$#,##0.00"),
        ("Unpaid Overdue Total", f'=SUMIF(Invoices!H2:H{last_inv_row},"YES",Invoices!D2:D{last_inv_row})', "$#,##0.00"),
        ("Unpaid Overdue Count", f'=COUNTIF(Invoices!H2:H{last_inv_row},"YES")', "0"),
    ]
    for offset, (label, formula, num_fmt) in enumerate(metrics, start=5):
        ws_sum.cell(row=offset, column=1, value=label).font = bold_font
        val_cell = ws_sum.cell(row=offset, column=2, value=formula)
        val_cell.font = body_font
        val_cell.number_format = num_fmt

    # Highlight Budget Remaining red if negative, green if >= 0
    ws_sum.conditional_formatting.add(
        "B8:B8", FormulaRule(formula=["B8<0"], fill=overdue_fill, font=overdue_font)
    )
    ws_sum.conditional_formatting.add(
        "B8:B8", FormulaRule(formula=["B8>=0"], fill=ok_fill, font=ok_font)
    )

    # Spend by Vendor table
    vendor_start_row = 12
    ws_sum.cell(row=vendor_start_row, column=1, value="Spend by Vendor").font = section_font
    for col_idx, col_name in enumerate(["Vendor", "Total Spend", "Unpaid Overdue", "Invoice Count"], start=1):
        c = ws_sum.cell(row=vendor_start_row + 1, column=col_idx, value=col_name)
        c.fill = header_fill
        c.font = header_font

    vendors = sorted({r["Vendor"] for r in rows})
    first_v_row = vendor_start_row + 2
    for i, vendor in enumerate(vendors):
        r_num = first_v_row + i
        ws_sum.cell(row=r_num, column=1, value=vendor).font = body_font

        c_tot = ws_sum.cell(
            row=r_num,
            column=2,
            value=f'=SUMIF(Invoices!$B$2:$B${last_inv_row},A{r_num},Invoices!$D$2:$D${last_inv_row})',
        )
        c_tot.number_format = "$#,##0.00"
        c_tot.font = body_font

        c_ov = ws_sum.cell(
            row=r_num,
            column=3,
            value=f'=SUMIFS(Invoices!$D$2:$D${last_inv_row},Invoices!$B$2:$B${last_inv_row},A{r_num},Invoices!$H$2:$H${last_inv_row},"YES")',
        )
        c_ov.number_format = "$#,##0.00"
        c_ov.font = body_font

        c_cnt = ws_sum.cell(
            row=r_num,
            column=4,
            value=f'=COUNTIF(Invoices!$B$2:$B${last_inv_row},A{r_num})',
        )
        c_cnt.number_format = "0"
        c_cnt.font = body_font

    last_v_row = first_v_row + len(vendors) - 1
    check_row = last_v_row + 2
    ws_sum.cell(row=check_row, column=1, value="Reconciliation Check").font = bold_font
    c_chk = ws_sum.cell(
        row=check_row,
        column=2,
        value=f'=IF(ROUND(SUM(B{first_v_row}:B{last_v_row})-B5,2)=0,"OK","MISMATCH — NEW VENDOR?")',
    )
    c_chk.alignment = Alignment(horizontal="center")
    ws_sum.conditional_formatting.add(
        f"B{check_row}:B{check_row}",
        FormulaRule(formula=[f'B{check_row}="OK"'], fill=ok_fill, font=ok_font),
    )
    ws_sum.conditional_formatting.add(
        f"B{check_row}:B{check_row}",
        FormulaRule(formula=[f'B{check_row}<>"OK"'], fill=overdue_fill, font=overdue_font),
    )

    # ------------------------------------------------------------------
    # Sheet 3: Please_Check (audit log of every fix & guess)
    # ------------------------------------------------------------------
    ws_chk = wb.create_sheet("Please_Check")
    chk_headers = ["Severity", "Invoice_ID", "Issue", "Action_Taken"]
    ws_chk.append(chk_headers)
    for col_idx in range(1, len(chk_headers) + 1):
        c = ws_chk.cell(row=1, column=col_idx)
        c.fill = header_fill
        c.font = header_font

    for row_idx, item in enumerate(review_items, start=2):
        ws_chk.append([item["Severity"], item["Invoice_ID"], item["Issue"], item["Action_Taken"]])
        for col_idx in range(1, 5):
            ws_chk.cell(row=row_idx, column=col_idx).font = body_font

    if review_items:
        ws_chk.conditional_formatting.add(
            f"A2:D{len(review_items) + 1}",
            FormulaRule(formula=['$A2="PLEASE CHECK"'], fill=warn_fill, font=warn_font),
        )
    ws_chk.freeze_panes = "A2"

    # Auto-fit column widths gently across all sheets
    for ws in (ws_inv, ws_sum, ws_chk):
        for col in ws.columns:
            col_letter = get_column_letter(col[0].column)
            max_len = 10
            for cell in col:
                val = "" if cell.value is None else str(cell.value)
                if val.startswith("="):
                    val = "$99,999.00"
                max_len = max(max_len, len(val))
            ws.column_dimensions[col_letter].width = min(max_len + 4, 48)

    wb.save(out_path)


def main() -> None:
    rows, review_items = load_and_clean(INPUT_CSV)
    build_workbook(rows, review_items, OUTPUT_XLSX)

    total_spend = sum(r["Amount"] for r in rows)
    overdue = [r for r in rows if r["Status"] == "Unpaid" and r["Due_Date"] < AS_OF_DATE]
    print(f"Wrote {OUTPUT_XLSX}")
    print(f"Cleaned rows: {len(rows)} (from 18 raw)")
    print(f"Total spend:  ${total_spend:,.2f} (Budget remaining: ${BUDGET_USD - total_spend:,.2f})")
    print(f"Overdue:      {len(overdue)} invoices totaling ${sum(r['Amount'] for r in overdue):,.2f}")
    print(f"Review items: {len(review_items)}")


if __name__ == "__main__":
    main()
