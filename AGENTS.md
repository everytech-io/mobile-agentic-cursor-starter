# Project instructions for Cursor Agent

You are helping a learner transition from **mobile developer** to **AI engineer**.

**Primary app:** [ShipGate](shipgate/) — pre-ship checklist, leveled core → API → CLI.  
Optional legacy iOS sandbox: `sample-app/` (do not prioritize unless learner asks).

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

VERIFY and REVIEW run **in parallel** after a diff exists.

## Stack (ShipGate)

- **Python 3.9+**, FastAPI, pytest, httpx TestClient
- **Layout:**
  - `shipgate/shipgate/core/` — domain (Level 1)
  - `shipgate/shipgate/api/` — REST (Level 2)
  - `shipgate/shipgate/cli/` — terminal (Level 3)
  - `shipgate/tests/` — eval suite
- **Primary verifier:** `cd shipgate && ./scripts/verify.sh` or `pytest -q`

## Intentional gaps (do not fix unless exercise requires)

| Gap | Exercise |
|-----|----------|
| `empty_message()` returns blank | 02 |
| `get_item_detail()` + GET item route | 03 |
| Toggle from FAILED jumps to PASSED | 05 |

## Workflow rules

1. Read `exercises/` and [docs/15-shipgate-levels.md](docs/15-shipgate-levels.md) before large changes.
2. Minimal diffs — one exercise scope at a time.
3. No new dependencies unless exercise asks.
4. After edits: **parallel verify** — pytest/curl, human diff, suggest `/review-bugbot` on `shipgate/`; LEARNINGS.md.

## Skills

- `.cursor/skills/shipgate-core/` — Python + gap rules
- `.cursor/skills/verify-after-edit/` — parallel verify ritual

## Repo layout

- `docs/` — curriculum (start: 15-shipgate-levels, 00-ai-engineer-mindset)
- `exercises/` — hands-on
- `LEARNINGS.md` — append-only regression log
