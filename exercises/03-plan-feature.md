# Exercise 03 — Item detail (Level 1 → 2 bridge)

**Goal:** Multi-file feature with Plan Mode — domain + API route.  
**Time:** ~90 minutes  
**Level:** L1 Core + L2 API  
**Read first:** [docs/03-plan-mode.md](../docs/03-plan-mode.md)

## Spec

```
Plan Mode: Add checklist item detail for ShipGate.

## Done when
- [ ] ChecklistStore.get_item_detail() returns: label, status, blocking_reason (empty string if passed)
- [ ] GET /checklists/{id}/items/{item_id} returns JSON detail
- [ ] pytest tests/test_core.py::test_get_item_detail_returns_fields passes
- [ ] pytest tests/test_api.py::test_item_detail_route_missing_until_exercise_03 passes (update test name if you rename it)
- [ ] Full: pytest -q — all tests green

## Out of scope
- Persistence
- Auth
- New dependencies
```

## Steps

1. **Shift+Tab** → Plan Mode
2. Paste spec; save plan to `docs/plans/`
3. Approve build — core first, then API route
4. **Parallel verify:** `pytest -q` + Bugbot

## Plan prompt hint

```
@shipgate/shipgate/core/store.py @shipgate/shipgate/api/app.py @shipgate/tests/
Keep API handlers thin. blocking_reason explains why item blocks ship if not passed.
```

## Capture

LEARNINGS: Was Plan Mode faster than prompt-fixing?

Next: [04-capture-learning.md](04-capture-learning.md)
