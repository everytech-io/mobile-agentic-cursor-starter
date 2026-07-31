---
name: shipgate-core
description: ShipGate Python conventions and exercise gaps. Use when editing shipgate/**/*.py for Levels 1–2.
paths: shipgate/**/*.py
---

# ShipGate core conventions

- Python 3.9+; type hints; keep functions small.
- Domain lives in `shipgate/core/` — no FastAPI imports in core.
- API layer in `shipgate/api/` — thin handlers, delegate to `ChecklistStore`.
- **Do not fix exercise gaps early:**
  - `empty_message()` — Exercise 02
  - `get_item_detail()` + GET item route — Exercise 03
  - `toggle_item_passed` FAILED→PASSED bug — Exercise 05
- After edits, remind **parallel verify:**
  - `cd shipgate && pytest -q` or `./scripts/verify.sh`
  - human diff review
  - `/review-bugbot` on `shipgate/`
