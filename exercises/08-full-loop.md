# Exercise 08 — Full loop (Level 2 capstone)

**Goal:** End-to-end feature on API layer with all modes.  
**Time:** ~90 min  
**Level:** L2 API  
**Read first:** [docs/08-cursor-modes.md](../docs/08-cursor-modes.md), [docs/15-shipgate-levels.md](../docs/15-shipgate-levels.md)

## Feature (pick one)

**A.** `GET /checklists/{id}/blockers` — list items not PASSED with blocking_reason  
**B.** `POST /checklists/{id}/approve` — sets all items PASSED if none FAILED (else 409)  
**C.** Your choice — one endpoint, one done-when

## Required sequence

| Step | Mode | Action |
|------|------|--------|
| 1 | Ask | Explore where logic should live (core vs api) |
| 2 | Plan | Save plan to `docs/plans/` |
| 3 | Agent | Implement + tests in `tests/test_api.py` |
| 4 | Verify ∥ Review | `pytest -q`, curl example, Bugbot |
| 5 | Capture | LEARNINGS + skill/AGENTS update if needed |

## Done when

- [ ] New test(s) in `tests/test_api.py`
- [ ] curl one-liner in LEARNINGS or plan doc proves behavior
- [ ] `/review-bugbot` run in parallel
- [ ] Can explain Level 1 vs 2 vs 3 from [15-shipgate-levels.md](../docs/15-shipgate-levels.md)

**Level 3 CLI stretch:** wire `shipgate check` to hit API instead of in-memory store (optional).

Graduation: [09-ai-engineer-graduation.md](09-ai-engineer-graduation.md)
