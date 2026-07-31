# Release Ready — product levels

**Product:** [PRODUCT.md](../PRODUCT.md) — *Can we ship this build?*

You build **one product** in four levels. Same story, more surface area.

```
L1 CORE   “Is the logic correct?”     pytest
L2 API    “Can other tools ask?”      pytest + curl
L3 CLI    “Can CI block deploy?”      exit code
L4 YOU    “Does it fit our stack?”     your verifiers / MCP
```

---

## Level 1 — Core (Week 1)

**Ships:** Python domain — checklists, items, `ready_to_ship`, messages.

| Exercise | Feature you add |
|----------|-----------------|
| 01 | Explore only |
| 02 | Friendly message when checklist has zero items |
| 03 | Item detail (label, status, blocking reason) |
| 04–06 | AGENTS.md + verify ritual |

**Verifier:** `cd release-ready && pytest tests/test_core.py -q`

**Starter:** 2 tests fail until Ex 02–03. Expected.

---

## Level 2 — API (Week 2)

**Ships:** HTTP API so teams/automation can query release status.

| Exercise | Feature |
|----------|---------|
| 03 (cont.) | `GET /checklists/{id}/items/{item_id}` |
| 05 | Fix FAILED → toggle bug |
| 08 | New endpoint (blockers list or approve flow) |

**Verifier:**

```bash
pytest tests/test_api.py -q
curl -s http://localhost:8000/checklists | python -m json.tool
```

---

## Level 3 — CLI (Week 2–3 bridge)

**Ships:** Pipeline gate — same decision as API, for CI.

```bash
release-ready list
release-ready check <checklist-id>   # 0 = ship, 1 = blocked, 2 = not found
```

Wire into AGENTS.md. Optional stretch: GitHub Action runs `./scripts/verify.sh`.

---

## Level 4 — Transfer (Week 3 graduation)

[Exercise 09](../exercises/09-ai-engineer-graduation.md) — pick one:

| Option | Example |
|--------|---------|
| **Extend Release Ready** | SQLite persistence; GitHub MCP pulls PR check status into a checklist |
| **Your product** | Same loop on your API, script, ticket — copy AGENTS.md pattern |

Graduation = verifier evidence on work **beyond** L2 capstone.

---

## Parallel verify (every level)

1. **Automated:** `./scripts/verify.sh` or level pytest/curl  
2. **Human:** diff + done-when path  
3. **Agent:** `/review-bugbot` on `release-ready/` — **parallel**, not after

[14-verification-practices.md](14-verification-practices.md)

---

## Optional: legacy iOS sandbox

[sample-app/](../sample-app/) — SwiftUI habit list, **not** Release Ready. Skip unless you want extra UI practice.

Next: [00-start-here.md](00-start-here.md)
