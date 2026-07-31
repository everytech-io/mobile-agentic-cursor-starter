# Expanded plan — 2026-08-01

> **Status:** Active curriculum (Week 1 + Week 2 shipped in repo)  
> **Repo:** [everytech-io/mobile-agentic-cursor-starter](https://github.com/everytech-io/mobile-agentic-cursor-starter)

## Mission

Teach rusty mobile developers the **full Cursor agentic surface** used in production:

- **AGENTS.md** — always-on project memory
- **Skills** — scoped workflows (`/create-skill`, `/ios-verify`, `/swiftui-exercises`)
- **Modes** — Ask, Agent, **Plan**, **Debug**
- **Review** — `/review-bugbot`, agent review before ship
- **Verify** — Xcode ⌘B/⌘R (non-negotiable for iOS)

---

## Delivered artifacts

| Artifact | Path | Status |
|----------|------|--------|
| Watch-first (Cursor Learn) | `docs/00-watch-first.md` | ✅ |
| Week 1 docs | `docs/00`–`06`, `05-verify` | ✅ |
| Week 2 docs | `docs/08`–`11` (modes, AGENTS, skills, debug/review) | ✅ |
| Exercises 01–08 | `exercises/` | ✅ |
| Sample app StarterApp | `sample-app/StarterApp/` | ✅ |
| AGENTS.md | root | ✅ |
| Skills (example) | `.cursor/skills/swiftui-exercises/`, `ios-verify/` | ✅ |
| Full syllabus | `docs/07-week-1-syllabus.md` | ✅ |
| Official links | `docs/official-cursor-links.md` | ✅ |

---

## Week 1 milestones (5–7 h learner time)

| # | Milestone | Acceptance |
|---|-----------|------------|
| W1.1 | Clone, watch, run StarterApp | ⌘R succeeds |
| W1.2 | Agent orient + empty state | Ex 01–02, LEARNINGS |
| W1.3 | Plan Mode detail screen | Plan saved optional; Ex 03 ships |
| W1.4 | AGENTS.md extended | Ex 04, 06 — verify ritual section |
| W1.5 | Dual-app cold verify | Ex 03 re-tested without notes |

---

## Week 2 milestones (4–6 h learner time)

| # | Milestone | Acceptance |
|---|-----------|------------|
| W2.1 | Skills literacy | Ex 07 — `ios-verify` skill exists |
| W2.2 | Debug Mode | Ex 05 — repro → fix → cleanup |
| W2.3 | Bugbot review | `/review-bugbot` on sample-app diff |
| W2.4 | Capstone full loop | Ex 08 — Ask → Plan → Agent → Review |
| W2.5 | Own app transfer | AGENTS.md + skills copied; one real feature |

---

## Mode routing (teaching script)

```
Understand only        → Ask
One screen, spec'd     → Agent
Multi-file / unclear   → Plan → Agent
Repro bug, unclear why → Debug
Before ship            → /review-bugbot
Always (iOS)           → Xcode verify
```

---

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Agent hallucinates SwiftUI APIs | AGENTS.md + swiftui-exercises skill; iOS 17 in every prompt |
| Learner skips Xcode | ios-verify skill; mentor checks LEARNINGS |
| Debug Mode weak on SwiftUI | Fallback: Ask + console paste (doc 11) |
| Intel Mac / no Xcode MCP | Document dual-app; MCP = optional Phase 4 |
| Rules confusion | Teach skills-first; rules = compliance only |
| Over-scoped capstone | Ex 08 options A/B are one-screen |

---

## Phase 3 — EveryTech packaging (next)

- [ ] Facilitator 1-pager (live workshop 3h vs async 2-week)
- [ ] Link from `everytech-products` README
- [ ] Pilot 3 learners; track time-to-first-⌘R
- [ ] Optional: recorded EveryTech walkthrough (modes demo)
- [ ] Optional: Android Studio parallel doc

---

## Phase 4 — Advanced opt-in

- [ ] Xcode MCP (M-series, Xcode 26.3+)
- [ ] MCP GitHub / Linear
- [ ] Cloud Agents
- [ ] Every* adapter mobile lesson

---

## Metrics (targets for pilot)

| Metric | Target |
|--------|--------|
| First verified Agent edit | < 90 min |
| Week 1 completion (Ex 1–4) | ≥ 70% |
| Week 2 completion (Ex 5–8) | ≥ 50% |
| Uses Plan + Debug + Bugbot once each | 100% of graduates |

---

## Revision log

| Date | Change |
|------|--------|
| 2026-08-01 | Initial expanded plan — full skills, AGENTS.md, Plan, Debug, Bugbot curriculum |
