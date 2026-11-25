# Invoice Cleanup Demo — LLM-Written Python vs. Hosted Spreadsheet Harnesses

A small, self-contained demo comparing a hosted AI spreadsheet tool (such as Anthropic's Claude Sheets) against having an LLM write a **deterministic Python script** that produces a native Excel workbook — complete with live formulas, a summary tab, a reconciliation check, a human-review tab, and **native Excel conditional formatting**.

Inspired by Dan Rice's AI Signal walkthrough (*"I gave Claude Sheets a messy invoice file"*).

---

## What is inside

| File | Description |
|---|---|
| `messy_invoices_sample.csv` | Synthetic 18-row Q4 marketing invoice file with 6 planted issues: 2 duplicate invoice IDs (`INV-403`, `INV-407`), currency amounts formatted as text (`"$3,200.00"` vs `8500`), mixed date formats (`2026-10-01` vs `10/10/2026`), sloppy vendor casing/whitespace (`" pixelcraft studio "`), 1 blank category (`INV-412`), and a paid invoice past its due date (`INV-414`). |
| `clean_invoices.py` | Deterministic `openpyxl` script that cleans the CSV and builds the Excel workbook. |
| `clean_invoices.xlsx` | Pre-generated output so you can open and test the live formulas and conditional formatting without running Python. |

---

## Run it yourself (no virtualenv needed)

With [`uv`](https://docs.astral.sh/uv/) installed:

```bash
uv run --with openpyxl python clean_invoices.py
```

Expected output:

```text
Cleaned rows: 16 (from 18 raw)
Total spend:  $39,750.00 (Budget remaining: $2,250.00)
Overdue:      4 invoices totaling $11,500.00
Review items: 4
```

---

## 30-second live test in Excel, Google Sheets, or LibreOffice

Open `clean_invoices.xlsx` in Excel, Google Sheets, or LibreOffice Calc (not macOS Finder QuickLook, which does not evaluate formulas):

1. **`Invoices` tab:** The 4 unpaid overdue rows (`INV-403`, `INV-406`, `INV-407`, `INV-410`) are highlighted red via a native Excel conditional formatting rule (`$H2="YES"`).
2. **Test live recalculation:** Change cell `F4` (`INV-403` Status) from `Unpaid` to `Paid`. `Overdue_Flag` flips to `NO`, **the red row highlight disappears live**, and `Summary` updates the overdue total from `$11,500` to `$7,000`.
3. **`Summary` tab:** Change cell `B3` (`As-Of Date`) from `2026-11-24` to `2026-11-26` (or `=TODAY()`). `INV-409` (due Nov 25) immediately turns red on `Invoices`.
4. **`Please_Check` tab:** Every automated fix is logged, with the inferred `Copywriting` category for `INV-412` highlighted yellow at the top for 1-minute human sign-off.

---

## The rule of thumb

- **One-off cleanup on a small, low-sensitivity file?** A hosted spreadsheet harness like Claude Sheets is great UX.
- **Recurring workflow (monthly close, reconciliations), thousands of rows, or anything an auditor might ask about?** Let the LLM build a deterministic script once, inspect it, put it under version control, and run the script — not the LLM — on your data.

More workshops and practical AI guides at [distantproximity.co.uk](https://distantproximity.co.uk).
