# Exercise 02 — Empty checklist message (Level 1)

**Goal:** One Agent edit, **parallel verify**, first green test.  
**Time:** ~30–45 minutes  
**Level:** L1 Core  
**Read first:** [docs/02-day-1-explore-and-edit.md](../docs/02-day-1-explore-and-edit.md), [docs/05-verify-loop.md](../docs/05-verify-loop.md)

## Spec (paste into Agent first)

```
## Goal
When a checklist has zero items, empty_message() returns helpful copy for an engineer about to ship.

## Done when
- [ ] pytest tests/test_core.py::test_empty_message_shows_helpful_copy passes
- [ ] Human: diff reviewed — only release-ready/release_ready/core/ changed (unless tests need one-line tweak)
- [ ] Agent review: /review-bugbot on release-ready/ (parallel with pytest)

## Out of scope
- API routes
- Database
- CLI changes
```

## Implementation prompt

```
Implement the spec above.
Match existing style in @release-ready/release_ready/core/store.py
Run pytest tests/test_core.py::test_empty_message_shows_helpful_copy when done.
```

## Verify (parallel lanes)

1. **Automated:** `cd release-ready && pytest tests/test_core.py::test_empty_message_shows_helpful_copy -q`
2. **Human:** read diff
3. **Agent review:** `/review-bugbot` on `release-ready/`

## Capture

Append to [LEARNINGS.md](../LEARNINGS.md):

```markdown
## YYYY-MM-DD — Exercise 02 empty_message
- Worked:
- Failed:
- Rule for next time:
```

Next: [03-plan-feature.md](03-plan-feature.md)
