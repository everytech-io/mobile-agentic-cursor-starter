# ShipGate levels — what you build when

**ShipGate** is a pre-ship checklist product. You grow it in **four levels** while learning the AI engineer loop. Same repo, same verifiers, harder scope.

```
Level 1  CORE     domain + unit tests          pytest tests/test_core.py
Level 2  API      REST + integration tests      pytest tests/test_api.py + curl
Level 3  CLI      terminal gate for CI          shipgate check <id> (exit code)
Level 4  TRANSFER your job / extend ShipGate     your verifiers + MCP optional
```

---

## Why this app (not a mobile UI)

| Mobile sandbox | ShipGate |
|----------------|----------|
| Xcode/simulator | `pytest`, `curl`, exit codes |
| UI empty state | Domain `empty_message()` |
| Navigation screen | API route + `get_item_detail()` |
| "Looks fine" | Tests red/green |

Mobile devs already know "build failed = not done." ShipGate generalizes that to **any stack**.

Optional legacy iOS sandbox: [sample-app/](../sample-app/) (not required).

---

## Level 1 — Core (Week 1, Level 1 graduate)

**Path:** `shipgate/shipgate/core/`  
**Verifier:** `cd shipgate && pytest tests/test_core.py -q`

| Exercise | You implement | Test that goes green |
|----------|---------------|----------------------|
| [01](../exercises/01-explore.md) | Orient only | — |
| [02](../exercises/02-small-change.md) | `ChecklistStore.empty_message()` | `test_empty_message_shows_helpful_copy` |
| [03](../exercises/03-plan-feature.md) | `get_item_detail()` + API route | `test_get_item_detail_*`, `test_item_detail_route_*` |
| [04](../exercises/04-capture-learning.md) | LEARNINGS + AGENTS.md | — |
| [06](../exercises/06-agents-md.md) | Verify ritual with `scripts/verify.sh` | — |

**Starter pytest:** 2 tests fail until Ex 02–03 done. That is intentional.

---

## Level 2 — API (Week 2, Level 2 graduate)

**Path:** `shipgate/shipgate/api/`  
**Verifier:** `pytest tests/test_api.py -q` + manual `curl`

| Exercise | Focus |
|----------|-------|
| [05](../exercises/05-debug-mode.md) | Fix toggle bug when item status is FAILED |
| [07](../exercises/07-create-skill.md) | `shipgate-core` / `verify-after-edit` skills |
| [08](../exercises/08-full-loop.md) | Full loop: new endpoint (e.g. ship blockers list) |

Example curl verify:

```bash
uvicorn shipgate.api.app:app --port 8000 &
curl -s http://localhost:8000/checklists | python -m json.tool
```

---

## Level 3 — CLI (Week 2–3 bridge)

**Path:** `shipgate/shipgate/cli/`  
**Verifier:** exit code

```bash
shipgate list
shipgate check <checklist-id>   # 0 = ready, 1 = not ready, 2 = not found
```

Wire CLI into AGENTS.md as CI-style verify. Optional stretch: GitHub Action that runs `scripts/verify.sh`.

---

## Level 4 — Transfer (Week 3, Level 3 graduate)

[Exercise 09](../exercises/09-ai-engineer-graduation.md) — pick one:

| Option | Task |
|--------|------|
| **A. Extend ShipGate** | Persistence (SQLite), auth stub, or MCP read of GitHub PR checks |
| **B. Your repo** | Same loop on telco script, internal API, ticket — copy AGENTS.md pattern |

Graduation requires **verifier evidence** on work that matters to you, not finishing every ShipGate level.

---

## Parallel verify (every level)

After every delegate step:

1. **Automated:** `scripts/verify.sh` or level-specific pytest/curl  
2. **Human:** read diff + walk done-when  
3. **Agent review:** `/review-bugbot` on `shipgate/` (parallel)

See [14-verification-practices.md](14-verification-practices.md).

---

## Setup

```bash
cd shipgate
uv venv && source .venv/bin/activate   # or: python3 -m venv .venv
uv pip install -e ".[dev]"               # or: pip install -e ".[dev]"
pytest -q                                 # expect 2 failures before Ex 02–03
./scripts/verify.sh
```

Next: [00-start-here.md](00-start-here.md)
