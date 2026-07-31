# ShipGate

**Pre-ship checklist** — the primary training app for this course. Not a mobile UI exercise.

You level up the **same product** while practicing the AI engineer loop. Every level adds a layer; verifiers stay explicit (`pytest`, `curl`, CLI exit code).

## Level map

| Level | Layer | Week | Verifier | You build |
|-------|-------|------|----------|-----------|
| **L1** | Core | 1 | `pytest tests/test_core.py` | Domain logic, empty checklist, item detail |
| **L2** | API | 2 | `pytest tests/test_api.py` + `curl` | REST endpoints, ship-ready gate |
| **L3** | CLI | 2–3 | `shipgate check …` exit code | Terminal workflow for CI |
| **L4** | Transfer | 3 | Your project's verifiers | Extend ShipGate or your real repo |

Full guide: [docs/15-shipgate-levels.md](../docs/15-shipgate-levels.md)

## Quick start

```bash
cd shipgate
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## Run API (Level 2+)

```bash
uvicorn shipgate.api.app:app --reload --port 8000
curl http://localhost:8000/checklists
```

## Intentional gaps (for exercises)

- **Ex 02:** `ChecklistStore.empty_message()` not implemented
- **Ex 03:** No `get_item_detail()` / no `GET .../items/{id}` route
- **Ex 05:** Bug when toggling items on empty-then-add checklist (Debug exercise)

Do not fix these until the matching exercise.
