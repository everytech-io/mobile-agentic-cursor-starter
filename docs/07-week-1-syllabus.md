# Full syllabus — Cursor agentic workflow for mobile devs

Two-week path: **Agent basics → AGENTS.md → Skills → Plan → Debug → Review → capstone**.

Official index: [official-cursor-links.md](official-cursor-links.md)  
Program plan: [HIGH-LEVEL-PLAN.md](HIGH-LEVEL-PLAN.md) · Expanded: [plans/2026-08-01-expanded-plan.md](plans/2026-08-01-expanded-plan.md)

---

## Week 1 — Loop + verify

| Day | Read | Exercise | Outcome |
|-----|------|----------|---------|
| 0 | [00-watch-first](00-watch-first.md) | — | Cursor Learn: Agents + Working with agents |
| 1 | [00-start-here](00-start-here.md), [01-install](01-install-and-open.md), [02-day-1](02-day-1-explore-and-edit.md) | [01](../exercises/01-explore.md), [02](../exercises/02-small-change.md) | Orient + one verified edit |
| 2 | [05-verify-loop](05-verify-loop.md) | Finish 02 | LEARNINGS #1 |
| 3 | [03-plan-mode](03-plan-mode.md), [08-cursor-modes](08-cursor-modes.md) | [03](../exercises/03-plan-feature.md) | Plan → detail screen |
| 4 | [04-rules-and-context](04-rules-and-context.md), [09-agents-md](09-agents-md.md) | [04](../exercises/04-capture-learning.md), [06](../exercises/06-agents-md.md) | AGENTS.md + LEARNINGS |
| 5 | [06-cursor-plus-xcode](06-cursor-plus-xcode.md) | Re-verify Ex 03 in Xcode only | Dual-app habit |

---

## Week 2 — Full Cursor surface area

| Day | Read | Exercise | Outcome |
|-----|------|----------|---------|
| 6 | [10-skills](10-skills.md) | [07](../exercises/07-create-skill.md) | `/create-skill` + `ios-verify` |
| 7 | [11-debug-and-review](11-debug-and-review.md) | [05](../exercises/05-debug-mode.md) | Debug Mode workflow |
| 8 | [08-cursor-modes](08-cursor-modes.md) | `/review-bugbot` on sample-app | Review gate |
| 9 | [08-cursor-modes](08-cursor-modes.md) | [08](../exercises/08-full-loop.md) | Ask → Plan → Agent → Review |
| 10 | — | Own app | Copy AGENTS.md + `.cursor/skills/` |

---

## Topic map (what you teach)

| Topic | Doc | Invoke / mode |
|-------|-----|-------------|
| Ask vs Agent | [08-cursor-modes](08-cursor-modes.md) | Ask mode |
| Agent + @ context | [04-rules-and-context](04-rules-and-context.md) | `@file` |
| **AGENTS.md** | [09-agents-md](09-agents-md.md) | root file |
| **Skills** | [10-skills](10-skills.md) | `/swiftui-exercises`, `/ios-verify`, `/create-skill` |
| **Plan Mode** | [03-plan-mode](03-plan-mode.md) | Shift+Tab → Plan |
| **Debug Mode** | [11-debug-and-review](11-debug-and-review.md) | Shift+Tab → Debug |
| **Bugbot / review** | [11-debug-and-review](11-debug-and-review.md) | `/review-bugbot` |
| Xcode verify | [05-verify-loop](05-verify-loop.md), [06-cursor-plus-xcode](06-cursor-plus-xcode.md) | ⌘B / ⌘R |

---

## Graduation checklist

- [ ] Exercises 01–08 complete (or 01–04 + 05–08 if skipping duplicates)
- [ ] AGENTS.md customized with verify ritual
- [ ] At least 2 skills in `.cursor/skills/` (swiftui-exercises + ios-verify or your own)
- [ ] One plan saved in `docs/plans/`
- [ ] Used Plan, Debug, and `/review-bugbot` at least once each
- [ ] Applied loop on **your** iOS project

---

## Mentor note

Teach **modes as routing**, not feature tourism. Every mode ends in **Xcode verify** for mobile.
