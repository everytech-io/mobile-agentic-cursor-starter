---
name: release-ready-core
description: Release Ready product conventions and exercise gaps. Use when editing release-ready/**/*.py (Levels 1–2).
paths: release-ready/**/*.py
---

# Release Ready — core conventions

Product: **Can we ship?** checklist engine. See [PRODUCT.md](../../PRODUCT.md).

- Python 3.9+; domain in `release_ready/core/` — no FastAPI in core.
- API in `release_ready/api/` — thin handlers → `ChecklistStore`.
- **Exercise gaps — do not fix early:**
  - `empty_message()` — Ex 02
  - `get_item_detail()` + GET item route — Ex 03
  - FAILED toggle bug — Ex 05
- **Parallel verify:** `cd release-ready && ./scripts/verify.sh`, human diff, `/review-bugbot` on `release-ready/`.
