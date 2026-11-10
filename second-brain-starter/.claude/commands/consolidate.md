---
description: Tidy the briefing rules and exceptions (run about once a month)
---

Tidy up what you have learned from my feedback, so the rules stay short, current and consistent. This is a review, not a rewrite: you propose, I decide.

Say in plain words what you're about to do: "I'll go through your briefing rules and exceptions, clear out what has expired, merge duplicates, and show you every change before I make it."

## 1. Checkpoint first

Run `git status`. If there are changes you didn't make, commit them as `My edits before <today>`. If this folder isn't a Git repository, stop and tell me to run the onboard command, which sets it up. Get the real date from the computer (see the briefing command) and use it for every date check below.

## 2. Read

Read `rulebook.md` (especially `## Briefing rules`, `## Exceptions` and `feedback_autonomy`), the frontmatter of every file in `projects/` (`status`, `paused_until`), and the open **Promise** Log entries (no later **Kept** entry) in `people/` and `projects/` that mention a date. Also look at the last 30 days of `git log --oneline` for commits whose message starts with `Feedback:`, to see what I have been telling you.

## 3. Find the problems

Make a list, in this order:

1. **Expired exceptions:** lines in `## Exceptions` whose `(until YYYY-MM-DD)` date has passed. Ask for each: has it ended, or should it be extended? Never decide for me.
2. **Paused projects due to restart:** `status: paused` with a `paused_until` date that has passed. Ask whether the project has restarted.
3. **Duplicates:** two or more rules that say the same thing.
4. **Contradictions:** two rules that can't both be true (for example "never show invoices" and "always show invoices from Acme"). Ask which one wins.
5. **Too broad:** a rule that hides more than the feedback behind it justified (for example "ignore all mail from this company" after I complained about one newsletter). Propose a narrower wording.
6. **Hiding too much:** any rule or exception that would hide a message that looks like phishing or a scam, a deadline in the next 3 days, anything legal or tax-related, or an overdue promise. Propose removing or narrowing it. These always win over my own rules.
7. **Too long:** if `## Briefing rules` has more than about 15 lines, suggest which could be grouped or dropped.

If there is nothing to tidy, say so in one line and stop.

## 4. Propose

Show the result as a short numbered list. For each item, give the **current wording**, the **proposed wording** (or "remove"), and **why**, in plain language. Don't change any file yet.

## 5. Apply what I approve

Make only the changes I say yes to, in `rulebook.md` and, for a restarted project, in that project's frontmatter (`status: active`, remove `paused_until`) with a dated Log entry. Never change `AGENTS.md`, `CLAUDE.md` or the commands. Then make a Git checkpoint: `git add -A` and `git commit -m "Feedback: consolidated rules"` as one command line.

Finish in chat with a two-line summary of what changed, and remind me that I can say "undo that" if I change my mind.
