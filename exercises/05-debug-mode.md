# Exercise 05 — Debug toggle bug (Level 2)

**Goal:** Debug Mode for reproducible domain bug.  
**Time:** ~60 min  
**Level:** L2 API/Core  
**Read first:** [docs/11-debug-and-review.md](../docs/11-debug-and-review.md)

## Bug (intentional in starter code)

When a checklist item is **FAILED**, calling `toggle_item_passed` sets it to **PASSED** instead of **PENDING** first.

## Spec

```
Debug Mode:

Bug: toggle_item_passed on a FAILED item marks it PASSED; should reset to PENDING.

Repro:
1. Create checklist with one item via store or API
2. set_item_status(..., FAILED)
3. toggle_item_passed(...)
4. Observe status is PASSED (wrong)

Expected: PENDING after toggle from FAILED

@release-ready/release_ready/core/store.py

Fix minimally. Add or update a pytest that locks correct behavior.
Parallel verify: pytest -q + Bugbot.
```

## Steps

1. **Shift+Tab** → Debug
2. Reproduce with pytest or API
3. Fix + add regression test
4. Parallel verify

## Capture

LEARNINGS: Did Debug beat guess-and-check?

Next: [06-agents-md.md](06-agents-md.md)
