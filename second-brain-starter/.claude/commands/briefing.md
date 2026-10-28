---
description: Create today's daily briefing in daily/YYYY-MM-DD.md
---

Create today's daily briefing. First read `rulebook.md` (style, what counts as urgent, which sources you can access) and `about-me.md`. Then read every file in `projects/` with `status: active`, and the most recent note in `daily/` if there is one.

Gather, from the sources available in this session:

1. **Calendar** — today's events and anything important in the next 3 days (if connected). The same meeting can appear twice (an invitation plus my own copy) — list it once. Flag invitations I haven't answered.
2. **Email** — new email since the last briefing (if connected; search by date, e.g. `newer_than:1d` or `after:` the last briefing, rather than just "latest"). Triage every message: match the sender against `people/` and the topic against `projects/`. Skip newsletters, marketing and FYI-only mail. Keep **at most 5** items that need action from me, each linked to a project or person.
   - **Read whole threads.** A mail search shows only one message per thread, often my own sent message. **Before you write "no reply", "awaiting response", "no news" or "no action needed" about any conversation, open the whole thread with the Gmail connector's (or plugin's) thread tool (get the thread by its id) and read every message in it.**
   - When you report a thread's status, give the date of its latest message ("Anna replied on 27 Oct") so a wrong "no reply" is easy to spot.
   - If you can't open a thread, say "could not verify" instead of guessing.
3. **Projects** — for each active project, the single most important next step, and anything overdue or stuck.
4. **People** — anyone I owe a reply to, open promises, birthdays in the next 7 days.

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

## Email — action items
- … → [[project-or-person]]

## Projects
- [[project]] — next step: …

## People
- …
```

Then:

- Add a dated **Log** entry to every project where you learned something new (newest first). If nothing is new (e.g. the first briefing right after onboarding), don't add an entry. Update a person's note if you learned something about them.
- **Don't send, reply to, delete or archive anything.** If a reply is needed, offer to draft it.
- If a source isn't connected, say so in one line in that section instead of guessing.
- Finish in chat with the Top 3 and a one-line list of the files you changed.
