# High-level plan — Mobile Agentic Cursor Starter

> **Status:** Skeleton for a planning subagent (e.g. **Fable**, Plan Mode, or dedicated planner) to expand.  
> **Repo:** https://github.com/everytech-io/mobile-agentic-cursor-starter  
> **Owner:** EveryTech — teach rusty mobile devs Cursor + agentic workflow

---

## Instructions for the planning subagent

You are **not** implementing code yet. Your job:

1. Read this file, [07-week-1-syllabus.md](07-week-1-syllabus.md), and the repo tree.
2. Expand each **Phase** below into milestones with owners, estimates, and acceptance criteria.
3. Output a detailed plan to `docs/plans/YYYY-MM-DD-expanded-plan.md` (create `docs/plans/` if needed).
4. Flag gaps in exercises, mentor materials, and learner assessments.
5. Do **not** rename the sample app, change bundle IDs, or add dependencies without explicit human approval.

**Suggested model / mode:** Cursor Plan Mode, or a planning-focused subagent (Fable) with read-only repo access first.

---

## Mission

Give a **rusty mobile developer** a repeatable loop:

```
ORIENT → SPEC → PLAN → IMPLEMENT (Agent) → VERIFY (Xcode) → CAPTURE (LEARNINGS)
```

No Xcode MCP required. Intel + Apple Silicon supported.

---

## Audience

| Attribute | Detail |
|-----------|--------|
| Background | Built iOS/Android before; away from daily coding |
| Gap | Used ChatGPT for snippets; never ran Agent with verify discipline |
| Success | Can ship one verified change/day using Cursor + Xcode |
| Not for | Greenfield CS students; advanced agent orchestration |

---

## Current state (shipped)

| Area | Status | Location |
|------|--------|----------|
| Week 1 docs | Done | `docs/00-watch-first` → `docs/07-week-1-syllabus` |
| Exercises 01–04 | Done | `exercises/` |
| Sample app **StarterApp** | Done | `sample-app/StarterApp/` — habit list, in-memory |
| AGENTS.md + skill | Done | root + `.cursor/skills/swiftui-exercises/` |
| Official links index | Done | `docs/official-cursor-links.md` |
| GitHub (public) | Done | `everytech-io/mobile-agentic-cursor-starter` |

**Intentional app gaps (for exercises):** no empty state (Ex 02), no detail screen (Ex 03).

---

## Phases (expand these)

### Phase 0 — Pre-flight (learner, ~30 min)

- [ ] Watch/read [00-watch-first.md](00-watch-first.md) (Cursor Learn: Agents + Working with agents)
- [ ] Install Cursor + Xcode; clone repo; run StarterApp once (⌘R)

**Planner deliverable:** Confirm prerequisites checklist; add troubleshooting FAQ if gaps found.

---

### Phase 1 — Week 1 core (learner, ~5–7 hours)

| Day | Focus | Exercise | Verify gate |
|-----|-------|----------|-------------|
| 1 | Orient + one edit | 01, 02 | Xcode ⌘B/⌘R |
| 2 | Verify discipline | 02 finish | LEARNINGS #1 |
| 3 | Plan Mode | 03 | Detail screen works |
| 4 | AGENTS.md + skills | 04 | 3× LEARNINGS |
| 5 | Dual-app ritual | 06 | Cold verify Ex 03 |

**Planner deliverable:** Mentor runbook (1-pager), rubric for "done", common failure modes + fixes.

---

### Phase 2 — Week 2 apply (learner → own app)

- [ ] Copy `AGENTS.md` + skill pattern into learner's real project
- [ ] One real feature using same loop (spec → plan → agent → xcode)
- [ ] Optional: SwiftLint in verify stack

**Planner deliverable:** Week 2 exercise template; "graduation" checklist; Android-side note (Cursor + Android Studio) if in scope.

---

### Phase 3 — Mentor / EveryTech packaging

- [ ] Slide deck or 1-page facilitator guide
- [ ] Link from `everytech-products` or internal LMS
- [ ] Cohort format (live vs async)
- [ ] Feedback form → iterate LEARNINGS patterns into skill updates

**Planner deliverable:** Launch checklist, metrics (completion, time-to-first-verify), content calendar.

---

### Phase 4 — Optional advanced (explicit opt-in)

- [ ] Xcode MCP track (M-series + Xcode 26.3+ only) — separate doc, not Week 1
- [ ] MCP: GitHub, Linear for PR workflow
- [ ] Subagents / Cloud Agents for long tasks
- [ ] Every* adapter lesson for mobile SDK integrations

**Planner deliverable:** Branching syllabus; prerequisites matrix; what NOT to teach on Day 1.

---

## Constraints (non-negotiable)

- **Xcode is source of truth** for iOS verify — never skip ⌘R in Week 1.
- **No rules-first** — prefer `AGENTS.md` + skills; rules only for org compliance.
- **Minimal sample app** — exercises teach workflow, not architecture.
- **No secrets** in repo; no production APIs in sample app.
- **Public repo** — scrub EveryTech-internal references before publish.

---

## Metrics (planner: define targets)

| Metric | Baseline | Target (suggest) |
|--------|----------|------------------|
| Time to first successful ⌘R after Agent edit | ? | < 90 min |
| Exercises 01–04 completion rate | 0 | TBD |
| Learners with 3+ LEARNINGS entries | 0 | TBD |
| Mentor NPS / "would recommend" | — | TBD |

---

## Open questions for planner

1. Single 1-day workshop vs self-paced Week 1 — which is primary?
2. Include Android (Kotlin/Compose) parallel track or iOS-only v1?
3. Rename repo / add `everytech.dev` landing page?
4. Video: embed Lee Robinson links vs record EveryTech walkthrough?
5. Certification badge / completion artifact?
6. Integrate with `the-every-ai-stack` marketplace skills?

---

## Acceptance criteria (program v1 complete)

- [ ] Rusty mobile dev completes Ex 01–04 without mentor intervention (pilot n≥3)
- [ ] All docs reference **StarterApp** consistently (no legacy HabitPeek naming)
- [ ] Expanded plan exists in `docs/plans/` with Phase 2–4 detail
- [ ] README links to this HIGH-LEVEL-PLAN and planner handoff section
- [ ] Sample app builds on Xcode 15+ / iOS 17 simulator

---

## Handoff prompt (copy to Fable / Plan Mode)

```
Read docs/HIGH-LEVEL-PLAN.md and the full repo.

Expand Phase 2–4 into a detailed implementation plan:
- Milestones with time estimates
- Mentor facilitator guide outline
- Week 2 exercise for learner's own app
- Risk register (Intel Mac, signing, Agent hallucinations)
- Recommended order of operations for the next 2 weeks of content work

Write output to docs/plans/YYYY-MM-DD-expanded-plan.md.
Do not change sample-app code in this pass.
```

---

## Revision log

| Date | Author | Change |
|------|--------|--------|
| 2026-08-01 | Cursor agent | Initial skeleton + StarterApp rename |
