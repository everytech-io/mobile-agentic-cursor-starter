# Start here

Welcome. This repo teaches **agentic development with Cursor** for mobile developers who feel rusty — not "how to prompt ChatGPT."

You will use **two apps**:

| App | You use it for |
|-----|----------------|
| **Cursor** | Spec, Agent, Plan Mode, AGENTS.md, reviewing diffs |
| **Xcode** | Build, run, debug — the source of truth |

You do **not** need Xcode MCP or an M-series Mac for this course.

## Before you begin

- [ ] [Watch/read the two Cursor Learn lessons](00-watch-first.md) (~15 min)
- [ ] [Cursor](https://cursor.com/downloads) installed and signed in
- [ ] Xcode installed
- [ ] This repo cloned and opened in Cursor (`File → Open Folder`)
- [ ] Sample app opens in Xcode and runs once:

```bash
open sample-app/StarterApp/StarterApp.xcodeproj
```

Press **⌘R** on iPhone simulator. You should see **StarterApp** (the sample habit tracker) with two habits.

## How to use this repo

1. Read docs **in order** (`docs/01` → `docs/06`).
2. Do the matching **exercise** in `exercises/` the same day.
3. After each session, append **one entry** to [LEARNINGS.md](../LEARNINGS.md).
4. Official Cursor reference: [official-cursor-links.md](official-cursor-links.md).

## The workflow (every session)

```
ORIENT  → Ask Agent to explain, or read the exercise brief
SPEC    → Goal + done-when + out-of-scope (exercises include templates)
PLAN    → Plan Mode (Shift+Tab) for multi-file work
BUILD   → Agent edits; you review diffs
VERIFY  → Xcode ⌘B and ⌘R — never skip this
CAPTURE → One LEARNINGS.md entry
```

4. Read [08-cursor-modes.md](08-cursor-modes.md) once you finish Week 1 — mode map for Plan / Debug / review.

## Day 1 (today)

| Step | Link | Time |
|------|------|------|
| 1 | [01-install-and-open.md](01-install-and-open.md) | 15 min |
| 2 | [Exercise 01](../exercises/01-explore.md) | 20 min |
| 3 | [02-day-1-explore-and-edit.md](02-day-1-explore-and-edit.md) | 15 min |
| 4 | [Exercise 02](../exercises/02-small-change.md) | 30 min |

## Mental model

**The Agent is a fast junior developer with terminal access.**

- It does not "know" your app until it reads files.
- It will confidently write wrong SwiftUI APIs unless you constrain it (AGENTS.md, skills, deployment target, review).
- **Your job:** spec, review, verify in Xcode, capture learnings.

That is agentic engineering — not vibe coding.

## Stuck?

- Agent hallucinating paths → `@sample-app/StarterApp/` to pin context
- Build fails in Xcode → paste the **exact** error into Agent
- Agent over-scoped → say "stop, only change `HabitListView.swift`"
- [Cursor troubleshooting — agent issues](https://cursor.com/help/troubleshooting/agent-issues.md)

Next: [01-install-and-open.md](01-install-and-open.md)
