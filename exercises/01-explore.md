# Exercise 01 — Explore ShipGate (Level 1)

**Goal:** Orient with Agent before writing code.  
**Time:** ~20 minutes  
**Level:** L1 Core  
**Verify:** No code changes required.

## Setup (once)

```bash
cd shipgate
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest -q    # note: 2 failures until Ex 02–03
```

## Steps

1. Open Cursor on repo root.
2. Open Agent (**⌘I**).
3. Paste:

```
@shipgate/

Explain ShipGate like I'm a rusty dev returning to code after mobile-only work.
Include:
- What problem ShipGate solves (pre-ship checklist)
- Level 1 vs Level 2 vs Level 3 layers
- Where checklist domain logic lives
- File I'd open first to change empty-checklist behavior
- Intentional gaps left for exercises

Max 12 bullets.
```

4. Open each file Agent mentions — confirm paths exist.
5. Run `pytest tests/test_core.py -q` and note which tests fail (Exercise 02–03 targets).

## Success criteria

- [ ] You can name the domain module (`shipgate/core/store.py`)
- [ ] You understand **2 failing tests are intentional**
- [ ] You know the Level 1 verifier: `pytest tests/test_core.py`

## Reflect (LEARNINGS.md)

What did Agent get right? What was wrong or vague?

Next: [02-small-change.md](02-small-change.md)
