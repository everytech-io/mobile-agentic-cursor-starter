# Release Ready

**Can we ship?** — checklist engine with API and CLI.

Read the product brief first: [../PRODUCT.md](../PRODUCT.md)

## Setup

```bash
cd release-ready
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest -q    # 2 failures until Exercises 02–03
```

## Levels (in this folder)

| Level | Path | Command |
|-------|------|---------|
| L1 | `release_ready/core/` | `pytest tests/test_core.py` |
| L2 | `release_ready/api/` | `uvicorn release_ready.api.app:app --port 8000` |
| L3 | `release_ready/cli/` | `release-ready check <id>` |

Map: [docs/15-product-levels.md](../docs/15-product-levels.md)

## Intentional gaps (exercises)

- **Ex 02:** `empty_message()` for zero-item checklists
- **Ex 03:** `get_item_detail()` + `GET .../items/{id}`
- **Ex 05:** toggle bug on FAILED items

Do not fix early.

## Verify

```bash
./scripts/verify.sh
```
