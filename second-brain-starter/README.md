# Second Brain Starter Kit

Workshop: **"Build a Second Brain"** — Distant Proximity

This folder becomes your second brain: a set of plain notes about your projects and the people in your life, kept up to date by your AI assistant. **You are the manager; the AI is the executor.**

## Choose your app

The same folder works in four apps. They differ in one important way: whether the AI can read your email and calendar directly.

| App | Notes in this folder | Gmail and Calendar | Works on | Where and who |
|-----|----------------------|--------------------|----------|---------------|
| **Claude** desktop app (Code tab) | Yes | Yes, with connectors | Mac, Windows | Claude Pro or Max |
| **ChatGPT** desktop app (Codex) | Yes | Yes, with plugins | Mac, Windows | Plus or higher recommended. Free and Go include Codex with lower limits, and plugins may not be available. |
| **Gemini** app for Mac (Task mode) | Yes, with connected folders | Yes, with Connected Apps | Apple Silicon Mac, macOS 15 or later | **Not available in the EEA, UK or Switzerland.** Google AI Pro or Ultra, personal Google account, 18 or over. |
| **Google Antigravity** app | Yes | **No direct connection.** You copy a summary across from Gemini (see below). | Mac, Windows | Works in Europe. Free with limits; Google AI Pro recommended. Personal Google account (work accounts need their admin). |

**Using Gemini in Europe, or on Windows?** Use Google Antigravity. The Gemini app can't connect a local folder there, so Antigravity is the closest route. Your notes, rules and briefing work the same way, but email and calendar reach the briefing only when you paste them in.

The workshop was first run on Claude. The ChatGPT, Gemini and Antigravity steps follow each company's documentation and haven't all had a full live run yet, so a menu may look slightly different. If it does, ask the host or the AI.

## Before the workshop

1. Your chosen **app**, installed and signed in:
   - Claude: https://claude.ai/download
   - ChatGPT: https://chatgpt.com/download (you may be asked to verify a phone number)
   - Gemini for Mac: https://gemini.google/desktop
   - Google Antigravity: https://antigravity.google
2. **Obsidian** (free): https://obsidian.md — for reading your notes.
3. Unzip this folder somewhere easy to find, e.g. `Documents/second-brain`. Don't put it in Google Drive or a shared cloud folder.
4. *Optional:* a **contact or client export** (CSV) from your CRM, e.g. Salesforce, HubSpot or LinkedIn. Keep the file handy: onboarding creates an `input/` folder, asks you to put it there, and uses it to set up your people and projects. A spoken braindump works too, with no preparation.
5. **Git** (required). It keeps a history of every change the AI makes, so you can see what changed and undo it. It works like version history in Google Docs and stays on your computer. You don't need to learn it.
   - **Claude, ChatGPT and Antigravity:** you don't have to do anything beforehand. The first thing onboarding does is check for Git, offer to install it if it's missing, and set up the history for this folder. If you decline, onboarding stops.
   - **Gemini app:** the AI can't run commands there, so set it up yourself before the workshop. Install [GitHub Desktop](https://desktop.github.com), choose **File → Add local repository**, pick the `second-brain` folder, and when it says the folder isn't a repository, click **create a repository**. During onboarding the AI will remind you to save a checkpoint (type a short message, then click **Commit**) after each step. Or ask the host to do it with you.
6. *Optional:* **uv**, a small free tool that helps with some later integrations. You don't have to do this beforehand: during onboarding, the AI checks whether it's installed and offers to install it for you. (This step is skipped in the Gemini app.)

## Getting started

**In the Claude app:**

1. Switch to the **Code** tab.
2. Choose this folder (`second-brain`) as the project folder.
3. Type **`/onboard`** and press Enter.

**In the ChatGPT app:**

1. Choose **Codex**, then add this folder (`second-brain`) as a project with **Add new project**.
2. Start a **New chat** in that project. Type `/permissions` and choose **Auto** or **Read-only**, never **Full access**.
3. Type **`$onboard`** and press Enter. If that doesn't show up, restart the app or just type "Start onboarding".

**In the Gemini app for Mac:**

1. Click **Task** below the text box. If Gemini doesn't offer it, it isn't available for your country or account; use Antigravity instead.
2. Under **Connected folders**, click the add-folder icon, choose this folder (`second-brain`) and allow access.
3. Paste this and send it:

   ```text
   Read AGENTS.md in my connected folder second-brain and follow it for this whole task. Then read .claude/commands/onboard.md in the same folder and follow it exactly.
   ```

**In Google Antigravity:**

1. Click **New Project**, then **Add Folder**, choose this folder (`second-brain`) and click **Create**. Choose **Local mode** if asked.
2. Set **Settings → General → Global Permissions → Permission Preset** to **Request Review** (the strictest). Never **Turbo**.
3. Type **`/onboard`** and press Enter. If that doesn't show up, just type "Start onboarding".

The AI starts by setting up Git (see above), then interviews you, a few questions at a time, and creates your notes as you go, saving a checkpoint after each step. You may be asked to approve the Git commands; that is expected. It takes about 45–75 minutes; you can stop any time and run onboarding again later to continue.

Then in Obsidian: **Open folder as vault** → choose the same folder, to browse your notes and the links between them.

## Every day after that

Each morning, run the briefing. Or just say "do my briefing".

| App | What to type |
|-----|--------------|
| Claude | `/briefing` |
| ChatGPT | `$briefing` |
| Antigravity | `/briefing` |
| Gemini app (new task, folder connected) | `Read AGENTS.md in my connected folder second-brain and follow it. Then do my briefing.` |

In Antigravity, the AI gives you a short prompt to paste into [gemini.google.com](https://gemini.google.com), which can read your Gmail and Calendar if you've turned on Google Workspace in its Connected Apps. You paste the answer back, and the briefing uses it.

Tell the AI when something changes ("I spoke to Anna — she'll send the quote by Friday"). Anything you type, paste or attach is considered for your notes: it files it in the right project or person note and tells you what it changed. Changes to the rulebook are only made the way you chose during onboarding (propose first, or apply and tell), and never silently.

**When the briefing is noisy or misses something, tell the AI in your own words, and say why.** For example: "You keep nagging me about the Acme invoice, but that project is on hold until January." It works out what to remember (a fact on the project note, a lasting preference, or a temporary exception), says back what it understood, and records it as a checkpoint you can undo. You never have to fill in a form.

About once a month, tidy up what it has learned:

| App | What to type |
|-----|--------------|
| Claude | `/consolidate` |
| ChatGPT | `$consolidate` |
| Antigravity | `/consolidate` |
| Gemini app | `Read AGENTS.md in my connected folder second-brain and follow it. Then consolidate my rules.` |

It lists rules that have expired, repeat each other or hide too much, and changes only what you approve.

**Undoing a change:** say "undo the last change" (or name what you want back). The AI shows what would be restored and asks before doing it.

## What's in here

| File | Purpose |
|------|---------|
| `AGENTS.md` | Standing instructions, read every session. ChatGPT and Antigravity read it directly; in the Gemini app, your first message asks it to. |
| `CLAUDE.md` | Tells the Claude app to read `AGENTS.md` |
| `.claude/commands/onboard.md` | The onboarding interview, used by every app |
| `.claude/commands/briefing.md` | The daily briefing, used by every app |
| `.claude/commands/consolidate.md` | The monthly tidy-up of your briefing rules, used by every app |
| `.agents/skills/` | Short pointers to those three files, so `$onboard` and `/onboard` work in ChatGPT and Antigravity |

Everything else (`about-me.md`, `rulebook.md`, `projects/`, `people/`, `daily/`, `input/`, `output/`, and the hidden `.git` history folder with its `.gitignore`) is created during onboarding. Never delete `.git`: it holds your history. Put files you want the AI to read in `input/`; anything it creates for you that isn't a note (PDFs, images, slides, drafts to publish or forward) lands in `output/`, in a subfolder per project where it fits.

Some of these files and folders start with a dot and may be hidden in Finder or Explorer. That's normal.

## Privacy and approvals

Your notes are plain files on your own computer. The AI reads them when you work with it in this folder, and what it reads is sent to the company behind your app so its AI can process it.

The rules in this folder tell the AI to ask before storing anything sensitive, and never to send, delete or spend anything without your approval. Your app's own approval prompts are the second safeguard, so keep them on:

- Don't choose **Full access** (ChatGPT), **Turbo** (Antigravity) or **Always allow** (any app).
- Decline any send or delete that you didn't ask for.

**Tools start read-only.** Onboarding sets every connected tool (Gmail, Calendar, Drive and so on) to the lowest level: it can read, and for email it can prepare drafts, but it can't send, delete, share or change anything. Onboarding also runs a safety test: it tries to delete a throwaway file and you check that your app stops it. The levels are written in your rulebook under `## Tool access`. Only you can raise one, by changing the app's setting and telling the AI, one tool at a time.

What your app can actually do changes often, so check the list on the connection's own settings page. Some apps let you set each action to *Always allow*, *Needs approval* or *Blocked*; if yours does, block everything that sends, replies, forwards, deletes, shares or changes events. If it doesn't, keep the approval prompts on and decline anything beyond reading and drafting.

Your history (Git) is a further safeguard for your notes: it lets you see and undo what the AI changed. It doesn't cover anything outside this folder, such as an email that was sent. Because it keeps old versions, deleting something from a note later doesn't remove it from the history, so don't ask the AI to write anything sensitive down "for now". The `input/` folder is left out of the history on purpose, and the history never leaves your computer unless you set that up yourself.

Check your app's data settings too, and don't put in anything you wouldn't want the company to process:

- **ChatGPT** (Plus and Pro): conversations may be used to improve models unless you turn that off in Data controls.
- **Antigravity**: Google may use and review your interactions unless you change this in Settings.
- **Gemini app**: Task mode needs Keep Activity turned on. See the Gemini Apps Privacy Hub for what that means.
- **Claude**: check your choice under Privacy in Settings.
