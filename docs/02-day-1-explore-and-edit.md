# Day 1: Explore and edit (ShipGate Level 1)

**Loop:** orient → spec → one change → parallel verify.

## Part A — Orient

See [Exercise 01](../exercises/01-explore.md).

## Part B — Spec before code

```
## Goal
Implement empty_message() for zero-item checklists.

## Done when
- [ ] pytest tests/test_core.py::test_empty_message_shows_helpful_copy passes
- [ ] Human diff reviewed
- [ ] /review-bugbot on shipgate/ (parallel)

## Out of scope
- API, CLI, database
```

## Part C — Implement

[Exercise 02](../exercises/02-small-change.md)

## Part D — Parallel verify

1. `pytest tests/test_core.py::test_empty_message_shows_helpful_copy -q`
2. Read diff
3. `/review-bugbot` on `shipgate/` — start while pytest runs

Paste full pytest output on failure.

## Part E — Capture

Append [LEARNINGS.md](../LEARNINGS.md).

Next: [15-shipgate-levels.md](15-shipgate-levels.md)
