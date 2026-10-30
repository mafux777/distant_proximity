---
description: Create today's daily briefing in daily/YYYY-MM-DD.md
---

Create today's daily briefing.

**Before anything else, get the real date and time from the computer.** Don't assume them. Run:

- Mac (and Git Bash on Windows): `date '+%A %Y-%m-%d %H:%M %Z'`
- Windows PowerShell: `Get-Date -Format 'dddd yyyy-MM-dd HH:mm K'`

Use the result for "today", the weekday, the note's file name, and every "in 2 hours" or "3 days ago" in the briefing.

Then read `rulebook.md` (style, what counts as urgent, which sources you can access) and `about-me.md`. Then read every file in `projects/` with `status: active`, and the most recent note in `daily/` if there is one.

Gather, from the sources available in this session:

1. **Calendar** — today's events and anything important in the next 3 days (if connected). The same meeting can appear twice (an invitation plus my own copy) — list it once. Flag invitations I haven't answered.
2. **Email** — new email since the last briefing (if connected; search by date, e.g. `newer_than:1d` or `after:` the last briefing, rather than just "latest"). Triage every message: match the sender against `people/` and the topic against `projects/`. Skip newsletters, marketing and FYI-only mail. Keep **at most 5** items that need action from me, each linked to a project or person.
   - **Read whole threads.** A mail search shows only one message per thread, often my own sent message. **Before you write "no reply", "awaiting response", "no news" or "no action needed" about any conversation, open the whole thread with the Gmail connector's (or plugin's) thread tool (get the thread by its id) and read every message in it.**
   - When you report a thread's status, give the date of its latest message ("Anna replied on 27 Oct") so a wrong "no reply" is easy to spot.
   - If you can't open a thread, say "could not verify" instead of guessing.
3. **Projects** — for each active project, the single most important next step, and anything overdue or stuck.
4. **People** — read the **Open loops** in `people/`. List anyone I owe a reply or a promise to, and anything others owe me that is now overdue. Use the `by` dates: overdue first, then due in the next 3 days. For every item, say who acts next.
   - **Going quiet:** people linked to an active project whose `last_contact` is more than 30 days ago (or empty). List at most 3, oldest first, with the project they matter for. Skip anyone I've said to leave alone.
5. **Who I'm meeting** — for each meeting today with people outside my household, look up every attendee in `people/` (match names, emails and `aliases`). Give their role and organisation, their part in the related project, and the latest Log entry or open loop. Flag attendees with no note and offer to create one.

Write `daily/<today>.md`:

```markdown
---
type: daily
date: <today>
---

# Briefing — <weekday, date>

## Top 3 today
1. …

## Calendar
- …

## Who I'm meeting
- [[person]] — role, organisation; part in [[project]]; last: …

## Email — action items
- … → [[project-or-person]]

## Projects
- [[project]] — next step: …

## People
- I owe [[person]]: …
- [[person]] owes me: … (overdue since …)
- Going quiet: [[person]] — last contact …, matters for [[project]]
```

For every item that someone else has to act on, end the line with `Next action: [[person]]` and don't give it a checkbox. Checkboxes are only for things I do myself. Never write "chase", "nudge" or "remind" as my action item.

Then:

- Add a dated **Log** entry to every project where you learned something new (newest first). If nothing is new (e.g. the first briefing right after onboarding), don't add an entry. Update a person's note if you learned something about them: a Log entry, `last_contact`, and their **Open loops** (tick off what was done).
- **Don't send, reply to, delete or archive anything.** If a reply is needed, offer to draft it.
- If a source isn't connected, say so in one line in that section instead of guessing.
- Finish in chat with the Top 3 and a one-line list of the files you changed.
