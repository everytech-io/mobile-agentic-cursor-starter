# Mobile → AI Engineer

**EveryTech** — transition **rusty mobile developers** into **AI engineers** who spec, engineer context, delegate to agents, verify with evidence, and ship — not just write screens faster.

[![EveryTech](https://img.shields.io/badge/org-everytech--io-blue)](https://github.com/everytech-io)

**StarterApp (SwiftUI)** is the Week 1–2 sandbox. **Week 3 graduation** is the same agentic loop on *your* real work (API, scripts, tickets, MCP).

| Phase | You learn |
|-------|-----------|
| **Mindset** | Mobile dev → AI engineer identity ([mindset doc](docs/00-ai-engineer-mindset.md)) |
| **Week 1–2** | Spec, context, modes, skills, Plan, Debug, review — via Cursor + Xcode |
| **Week 3** | Transfer loop to non-mobile work ([graduation exercise](exercises/09-ai-engineer-graduation.md)) |

## Start here

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .
```

1. **[AI engineer mindset](docs/00-ai-engineer-mindset.md)** — read this first
2. [Watch — Cursor Learn](docs/00-watch-first.md)
3. [Day 1 mechanics](docs/00-start-here.md)
4. [Competency map](docs/12-ai-engineer-competencies.md)

**Syllabus:** [docs/07-week-1-syllabus.md](docs/07-week-1-syllabus.md) (now 3-week arc)

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY → REVIEW → CAPTURE
```

| Layer | Tools |
|-------|--------|
| Context | AGENTS.md, skills, `@`, LEARNINGS, plans in git |
| Delegate | Ask / Agent / Plan / Debug, MCP (Week 3+) |
| Verify | Xcode (sandbox), then tests/scripts/PR on real work |
| Review | `/review-bugbot`, agent review |

Deep dive: [Context engineering](docs/13-context-engineering.md)

## Docs map

| Topic | Doc |
|-------|-----|
| Mindset shift | [00-ai-engineer-mindset](docs/00-ai-engineer-mindset.md) |
| Competencies + rubric | [12-ai-engineer-competencies](docs/12-ai-engineer-competencies.md) |
| Context engineering | [13-context-engineering](docs/13-context-engineering.md) |
| Modes | [08-cursor-modes](docs/08-cursor-modes.md) |
| AGENTS.md | [09-agents-md](docs/09-agents-md.md) |
| Skills | [10-skills](docs/10-skills.md) |
| Plan / Debug / Bugbot | [03](docs/03-plan-mode.md), [11](docs/11-debug-and-review.md) |

## Repo layout

```
docs/              # Mindset → competencies → mechanics → Week 3
exercises/         # 01–09 (09 = AI engineer graduation, non-mobile)
sample-app/        # StarterApp — training sandbox only
AGENTS.md          # Example always-on context
.cursor/skills/    # Example skills (promote patterns from LEARNINGS)
LEARNINGS.md       # Regression log → future skills
```

## Program plan

- [HIGH-LEVEL-PLAN.md](docs/HIGH-LEVEL-PLAN.md)
- [Expanded plan](docs/plans/2026-08-01-expanded-plan.md)

## License

MIT
