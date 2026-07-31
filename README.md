# Mobile Agentic Cursor Starter

**EveryTech** guided tutorial for rusty mobile developers learning **AI and agentic development with Cursor**.

[![EveryTech](https://img.shields.io/badge/org-everytech--io-blue)](https://github.com/everytech-io)

You do not need Xcode MCP or an M-series Mac. This course uses a proven dual workflow:

| Tool | Role |
|------|------|
| **Cursor** | Spec, Agent, Plan Mode, AGENTS.md, review |
| **Xcode** | Build, run, debug, sign, ship |

## Who this is for

- You built iOS/Android apps before but feel rusty
- You have used ChatGPT for snippets but not a real agent workflow
- You want a structured path, not random "vibe coding" tips

## Prerequisites

- [Cursor](https://cursor.com/downloads) installed and signed in
- **Xcode** installed (any recent version you already use for iOS)
- macOS (Intel or Apple Silicon — both work for this tutorial)
- Optional: [SwiftLint](https://github.com/realm/SwiftLint) (`brew install swiftlint`)

## Quick start (30 minutes)

1. **Clone and open in Cursor**
   ```bash
   git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
   cd mobile-agentic-cursor-starter
   cursor .
   ```

2. **Watch the two Cursor Learn lessons** → [docs/00-watch-first.md](docs/00-watch-first.md) (~15 min)

3. **Read the entry guide** → [docs/00-start-here.md](docs/00-start-here.md)

4. **Open the sample app in Xcode**
   ```bash
   open sample-app/StarterApp/StarterApp.xcodeproj
   ```
   Press **⌘R** once to confirm it runs on the simulator.

5. **Do Exercise 1 in Cursor** → [exercises/01-explore.md](exercises/01-explore.md)

## Repo structure

```
mobile-agentic-cursor-starter/
├── docs/                 # Guided workflow (read in order)
├── exercises/            # Hands-on tasks with prompts
├── sample-app/StarterApp # Tiny SwiftUI app for practice
├── LEARNINGS.md          # Your session log (append after each exercise)
├── AGENTS.md             # Project instructions for Cursor Agent
└── .cursor/skills/       # SwiftUI skill (loads when editing sample-app)
```

## Learning path

| Day | Doc | Exercise | Outcome |
|-----|-----|----------|---------|
| 1 | [01-install-and-open](docs/01-install-and-open.md) | [01-explore](exercises/01-explore.md) | Orient in a repo with Agent |
| 1 | [02-day-1-explore-and-edit](docs/02-day-1-explore-and-edit.md) | [02-small-change](exercises/02-small-change.md) | One verified change |
| 2 | [05-verify-loop](docs/05-verify-loop.md) | (same exercise) | Trust lint/build, not vibes |
| 3 | [03-plan-mode](docs/03-plan-mode.md) | [03-plan-feature](exercises/03-plan-feature.md) | Plan before multi-file edits |
| 4 | [04-rules-and-context](docs/04-rules-and-context.md) | [04-capture-learning](exercises/04-capture-learning.md) | AGENTS.md + skills + LEARNINGS |
| 5 | [06-cursor-plus-xcode](docs/06-cursor-plus-xcode.md) | Ship in Xcode | Full dual-app loop |

Full syllabus: [docs/07-week-1-syllabus.md](docs/07-week-1-syllabus.md)

Official Cursor docs index: [docs/official-cursor-links.md](docs/official-cursor-links.md)

## Core workflow (memorize this)

```
1. ORIENT   → Agent explains codebase (or read docs/00)
2. SPEC     → Write goal + done-when + out-of-scope
3. PLAN     → Plan Mode for anything > 1 file (Shift+Tab)
4. IMPLEMENT→ Agent edits; you review every diff hunk
5. VERIFY   → Xcode ⌘B / ⌘R (source of truth)
6. CAPTURE  → Append one entry to LEARNINGS.md
```

## Sample app

The Xcode project lives at `sample-app/StarterApp/`. The app’s **display name is HabitPeek** — a fictional mini habit tracker we use only for exercises (not a real product).

It shows a list of habits with streaks, in-memory storage, and **intentional gaps** for you to fix with Agent:

- No empty state (Exercise 02)
- No detail screen (Exercise 03)

The app is small on purpose. You practice **agent workflow**, not architecture.

## After Week 1

Apply the same loop to your own app (or fork this repo's pattern):

1. Copy `AGENTS.md` and `.cursor/skills/` into your project
2. Keep using Xcode for verify
3. Add skills or LEARNINGS entries only when the agent repeats the same mistake twice

## License

MIT — use freely for teaching and self-study.
