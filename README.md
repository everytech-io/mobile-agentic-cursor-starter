# Mobile Agentic Cursor Starter

**EveryTech** — full guided path for rusty mobile developers: **AGENTS.md, Skills, Plan Mode, Debug Mode, Bugbot review**, and Xcode verify.

[![EveryTech](https://img.shields.io/badge/org-everytech--io-blue)](https://github.com/everytech-io)

| Tool | Role |
|------|------|
| **Cursor** | Ask / Agent / Plan / Debug, skills, AGENTS.md, review |
| **Xcode** | Build, run, debug — source of truth |

## Quick start

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .
```

1. [Watch first — Cursor Learn](docs/00-watch-first.md) (~15 min)
2. [Start here](docs/00-start-here.md)
3. `open sample-app/StarterApp/StarterApp.xcodeproj` → **⌘R**
4. [Exercise 01](exercises/01-explore.md)

**Full syllabus (2 weeks):** [docs/07-week-1-syllabus.md](docs/07-week-1-syllabus.md)

## What you'll learn

| Topic | Doc |
|-------|-----|
| Cursor modes (Ask / Agent / Plan / Debug) | [docs/08-cursor-modes.md](docs/08-cursor-modes.md) |
| **AGENTS.md** | [docs/09-agents-md.md](docs/09-agents-md.md) |
| **Skills** (`/create-skill`, scoped skills) | [docs/10-skills.md](docs/10-skills.md) |
| **Plan Mode** | [docs/03-plan-mode.md](docs/03-plan-mode.md) |
| **Debug Mode** + **Bugbot** | [docs/11-debug-and-review.md](docs/11-debug-and-review.md) |
| Xcode verify loop | [docs/05-verify-loop.md](docs/05-verify-loop.md) |

## Repo layout

```
docs/           # 00-watch-first → 11-debug-and-review
exercises/      # 01–08 (capstone full loop)
sample-app/     # StarterApp — SwiftUI practice target
AGENTS.md       # Always-on agent instructions
.cursor/skills/ # swiftui-exercises, ios-verify (examples)
LEARNINGS.md    # Your session log
docs/plans/     # Saved plans + expanded program plan
```

## Core loop

```
ORIENT → SPEC → [Ask] → [Plan] → Agent → VERIFY (Xcode) → [/review-bugbot] → LEARNINGS
```

## Sample app

**StarterApp** — minimal in-memory habit list at `sample-app/StarterApp/`. Intentional gaps for exercises (empty state, detail screen). Not a shipped product.

## Program plan

- [HIGH-LEVEL-PLAN.md](docs/HIGH-LEVEL-PLAN.md) — mentor / planner skeleton
- [Expanded plan](docs/plans/2026-08-01-expanded-plan.md) — Week 1–2 milestones

## License

MIT
