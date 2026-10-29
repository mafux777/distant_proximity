# Second Brain Starter Kit

Workshop: **"Build a Second Brain with Claude"** — Distant Proximity

This folder becomes your second brain: a set of plain notes about your projects and the people in your life, kept up to date by your AI assistant. **You are the manager; the AI is the executor.**

The workshop is taught with **Claude**, but the same folder also works in the **ChatGPT desktop app (Codex)**. Steps for both are below.

## Before the workshop

1. A **paid plan**: Claude Pro or Max — or, if you use ChatGPT, a ChatGPT plan with Codex.
2. The **desktop app** (Mac or Windows), signed in:
   - Claude: https://claude.ai/download
   - ChatGPT: https://chatgpt.com/download
3. **Obsidian** (free): https://obsidian.md — for reading your notes.
4. Unzip this folder somewhere easy to find, e.g. `Documents/second-brain`.
5. *Optional:* a **contact or client export** (CSV) from your CRM, e.g. Salesforce, HubSpot or LinkedIn. Keep the file handy: onboarding creates an `input/` folder, asks you to put it there, and uses it to set up your people and projects. Email, calendar, team chat (Slack or Teams) and a spoken braindump work too, with no preparation.
6. *Optional:* **Git** and **uv**, two small free tools that help with some later integrations. You don't have to do this beforehand: during onboarding, the AI checks whether they're already installed and offers to install them for you.

## Getting started

**In the Claude app:**

1. Switch to the **Code** tab.
2. Choose this folder (`second-brain`) as the project folder.
3. Type **`/onboard`** and press Enter.

**In the ChatGPT app:**

1. Switch to the **Codex** view.
2. Open this folder (`second-brain`) as the project.
3. Type **`$onboard`** (or pick *onboard* from Skills) and press Enter. If that doesn't show up, just type "Start onboarding".

The AI will interview you, a few questions at a time, and create your notes as you go. It takes about 45–75 minutes; you can stop any time and run onboarding again later to continue.

Then in Obsidian: **Open folder as vault** → choose the same folder, to browse your notes and the links between them.

## Every day after that

- Each morning, run the briefing: **`/briefing`** in Claude, **`$briefing`** in ChatGPT (or just say "do my briefing").
- Tell the AI when something changes ("I spoke to Anna — she'll send the quote by Friday"). Anything you type, paste or attach is considered for your notes: it files it in the right project or person note and tells you what it changed. Changes to the rulebook are only proposed, never made silently.

## What's in here

| File | Purpose |
|------|---------|
| `AGENTS.md` | Standing instructions — read every session (ChatGPT reads it directly) |
| `CLAUDE.md` | Tells the Claude app to read `AGENTS.md` |
| `.claude/commands/onboard.md` | The onboarding interview (`/onboard` in Claude) |
| `.claude/commands/briefing.md` | The daily briefing (`/briefing` in Claude) |
| `.agents/skills/` | The same two commands for ChatGPT (`$onboard`, `$briefing`) |

Everything else (`about-me.md`, `rulebook.md`, `projects/`, `people/`, `daily/`, `input/`, `output/`) is created during onboarding. Put files you want the AI to read in `input/`; anything it creates for you that isn't a note (PDFs, images, slides, drafts to publish or forward) lands in `output/`, in a subfolder per project where it fits.

Some of these files and folders start with a dot and may be hidden in Finder or Explorer. That's normal.

## Privacy

Your notes are plain files on your own computer. The AI reads them when you work with it in this folder. It will ask before storing anything sensitive, and never sends, deletes or spends anything without your approval.
