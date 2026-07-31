# Exercise 08 — Full agentic loop (capstone)

**Goal:** Route modes correctly on one small feature end-to-end.  
**Time:** ~90 min  
**Read first:** [docs/08-cursor-modes.md](../docs/08-cursor-modes.md), [docs/14-verification-practices.md](../docs/14-verification-practices.md)

## Feature (pick one)

**A.** Habit row shows relative created date ("2 days ago")  
**B.** Swipe-delete shows confirmation alert  
**C.** Your choice (one screen, one outcome)

## Required mode sequence

| Step | Mode | Action |
|------|------|--------|
| 1 | **Ask** | Explore where date/formatting or alert logic should live |
| 2 | **Plan** | Write plan; save to workspace under `docs/plans/` |
| 3 | **Agent** | Implement approved plan only |
| 4 | **Verify ∥ Review** | Parallel: automated verifier + human diff/path + `/review-bugbot` |
| 5 | **Capture** | LEARNINGS + update AGENTS.md or skill if agent repeated a mistake |

## Plan prompt template

```
Plan Mode:

Feature: <A or B from above>

Done when:
- [ ] Named automated verifier green (document command)
- [ ] Manual test path documented
- [ ] Human diff review + Bugbot (parallel)
- [ ] No new dependencies

Save plan to workspace when approved.
@AGENTS.md @sample-app/
```

## Done when (capstone checklist)

- [ ] Used Ask, Plan, Agent, and parallel verify+review in one session
- [ ] Plan file exists in `docs/plans/`
- [ ] `/review-bugbot` run in parallel with other verifiers
- [ ] 4+ total LEARNINGS entries in repo
- [ ] Can explain mode map from [08-cursor-modes.md](../docs/08-cursor-modes.md) without notes

**Not graduation yet** — Week 3 [Exercise 09](09-ai-engineer-graduation.md) on **your real stack** with non-sandbox verifiers.
