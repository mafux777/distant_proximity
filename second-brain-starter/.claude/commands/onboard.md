---
description: Guided interview that sets up your second brain (resumable)
---

You are setting up a second brain for the person you're talking to. They are the manager; you are the executor. They are probably not technical — keep the language plain, friendly and short.

## How to interview

- Ask **2–3 questions at a time**, never a long questionnaire. Give a short example of a good answer when it helps.
- **Write files as you go.** After each block of answers, save them and show a short summary of what you wrote (not the whole file).
- Skipping is always fine. Write `TODO` for anything they skip and move on.
- **Never invent facts.** Only record what they told you.
- Ask before writing down anything sensitive (health, finances, ID numbers). Never store passwords. If they say something must not be stored, don't store it, and add a short general rule (not the information itself, e.g. "No health details") under `## Never write down` in `rulebook.md`.
- At the end of each step, set `onboarding_step: <N>` in the `about-me.md` frontmatter (N = the step just finished), say which step is next and ask if they're ready, or want a break. They can stop any time and type `/onboard` later to continue.

## Resume first

Before anything else, read `about-me.md`. If it doesn't exist, start at step 1. Otherwise read `onboarding_step` from its frontmatter and **continue with the next step** — or, if notes for the next step already exist (e.g. some projects but not all), pick up inside that step and ask what's missing. Tell the person where you're picking up.

If `onboarding_step` is 7, onboarding is complete: say so and suggest `/briefing`.

---

## Step 1 — Setup

Create the folders `projects/`, `people/`, `daily/`, and these starter files:

- `about-me.md` with frontmatter `type: profile`, `status: onboarding`, `onboarding_step: 1`, `created: <today>`.
- `rulebook.md` with frontmatter `type: rulebook`, `created: <today>`, a heading `# How we work together`, and an empty section `## Never write down`.

Then explain how the system works in **5 short bullet points** (manager/executor; one file per project and per person; links between them; a daily briefing; nothing is sent or deleted without approval). Mention that they can browse all of this in Obsidian by opening this folder as a vault.

Then ask if they're ready for step 2.

## Step 2 — About you → `about-me.md`

Cover, a few questions at a time:

1. Name, where they live, languages, and what they do right now (job, business, studies, retired, between jobs…).
2. Household and family — only what they want you to know.
3. Main email addresses and calendars, and the apps they use every day.
4. What a good week looks like for them, and what currently falls through the cracks.

Write `about-me.md` with sections **Identity**, **Work**, **Family & household**, **Accounts & tools**, **How I like to work**, **What falls through the cracks**. When done, give a 3-line summary of who they are, and ask them to correct anything wrong.

## Step 3 — Projects → `projects/*.md`

Explain: a project is anything with an outcome they care about in the next 3 months — work, job search, health, family, home, money, learning, a trip.

1. Ask them to **brain-dump** everything on their mind. Don't structure yet. Encourage messy lists.
2. Group what they said into **3–7 projects** and show the list (name + one-line goal) for approval. Merge, split or drop as they say.
3. For each approved project, create `projects/<short-name>.md`:

```markdown
---
type: project
status: active
priority: high | medium | low
created: <today>
tags: []
---

# <Project name>

## Goal
<one or two sentences>

## Current status
<where things stand>

## Next steps
- [ ] <concrete action>

## People
- <Name> — <role in this project>

## Log
- <today>: Project created during onboarding.
```

In step 3, write people as plain names; step 4 turns them into links. Ask one or two follow-up questions per project only where the goal or next step is unclear. Ask them to rank priorities if they didn't.

## Step 4 — People → `people/*.md`

Ask for the **5–8 people who matter most right now** (family, colleagues, clients, recruiters, friends, helpers). Start with the people already mentioned in projects. Tell them they can add more any time later just by mentioning someone. For each, capture: name, relationship, how they're in touch (only what they want stored), which projects they relate to, and anything worth remembering (birthday, last conversation, open promises in either direction).

Name files `people/<first-last>.md` when you know both names; otherwise use what they call the person (`herr-weber.md`, `mum-inge.md`). Don't ask questions just to complete a filename.

```markdown
---
type: person
status: active
created: <today>
tags: []
---

# <Full name>

**Relationship:** …
**Contact:** …
**Birthday:** … (if known)

## Projects
- [[project-name]]

## Notes
- …

## Log
- <today>: Added during onboarding.
```

In each project's **People** section, replace the plain names with links (`[[herr-weber]]`), and add anyone new — links on both sides.

## Step 5 — Ground rules → `rulebook.md`

Ask about:

1. What you may do on your own (e.g. update notes, draft emails, read their calendar).
2. What always needs their approval first (sending anything, deleting, spending, contacting people).
3. What stays private and must never be written down.
4. Preferred tone, language and level of detail for briefings.
5. What counts as "urgent" for them.

Write these into `rulebook.md` as sections `## What you may do on your own`, `## What needs my approval`, `## Never write down` (keep anything already there), `## Style`, `## What counts as urgent`. The approval rules may add to the ground rules in `CLAUDE.md` but never loosen them. Read the result back for confirmation.

## Step 6 — Email & calendar (optional)

Check whether you have Gmail / Google Calendar (or Outlook) **connector tools** in this session. Only connectors count — not command-line programs or anything else on the computer.

- **If yes:** read only. List their next 3 calendar events and the subjects of their 10 most recent emails to prove it works. Change nothing.
- **If not:** tell them: in the Claude app, open **Settings → Connectors**, connect Gmail and Google Calendar, then start a new session in this folder and type `/onboard` to come back here. Say the workshop host will show this on screen. Offer to continue without them for now — they can also paste emails or details into the chat.

Add a section `## Sources` to `rulebook.md` listing what you can access (e.g. "Gmail: read-only — connected", "Calendar: not connected").

## Step 7 — First daily briefing

Run the `/briefing` command's instructions (from `.claude/commands/briefing.md`) to create `daily/<today>.md`. Then:

- Offer to do one thing from the Top 3 right now, e.g. draft a message (draft only; they send it).
- Set `onboarding_step: 7` and `status: active` in `about-me.md`.
- Tell them that from tomorrow, they just type `/briefing`.
- Suggest 3 habits: run `/briefing` every morning; tell you whenever something changes ("I spoke to Anna, she agreed to…") so you update the notes; review `projects/` once a week.
- Congratulate them — their second brain is live.
