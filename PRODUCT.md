# Release Ready — the product

> **One sentence:** Release Ready answers *“Can we ship this build?”* by running a checklist of release gates and returning **ready** or **blockers**.

This repo is a **course** where you build Release Ready in four levels. The product is real; the scope grows each week.

---

## The problem

Before every release — TestFlight, staging deploy, production — someone asks:

- Are tests green?
- Is the changelog updated?
- Did staging smoke pass?
- Is rollback documented?

Today that lives in Slack threads, spreadsheets, and people’s heads. **Release Ready** makes it a small service teams can query and CI can gate on.

---

## The product (MVP)

| Capability | User | Output |
|------------|------|--------|
| **Checklists** | Release engineer | Named list of gates (items) |
| **Item status** | Engineer / automation | Each item: pending / passed / failed |
| **Ship decision** | CI or human | `ready_to_ship: true \| false` + why not |

### Example (Level 2 API)

```bash
curl http://localhost:8000/checklists/{id}/ready
# → {"ready_to_ship": false}

curl http://localhost:8000/checklists/{id}
# → items with status; empty checklist gets a clear message (Level 1)
```

### Example (Level 3 CLI)

```bash
release-ready check {checklist-id}
# exit 0 = READY (pipeline continues)
# exit 1 = NOT READY (pipeline stops)
```

---

## Who it’s for (story for learners)

| Persona | Uses Release Ready to… |
|---------|--------------------------|
| **Mobile dev (you)** | Same mental model as TestFlight gates — but as code + tests |
| **Release engineer** | One URL/CLI for go/no-go |
| **CI pipeline** | Block deploy if `release-ready check` fails |

Mobile background is an **asset**: you already think in “gates before ship.” This product codifies that.

---

## What you build — four levels

| Level | You ship | Verifier | Course week |
|-------|----------|----------|-------------|
| **L1 Core** | Domain logic: checklists, items, ready?, empty message | `pytest tests/test_core.py` | Week 1 |
| **L2 API** | REST API teams can call | `pytest tests/test_api.py` + `curl` | Week 2 |
| **L3 CLI** | `release-ready` for pipelines | exit code 0/1 | Week 2–3 |
| **L4 Transfer** | SQLite, GitHub checks, or **your company’s gate** | Your verifiers + MCP | Week 3 graduation |

Detail: [docs/15-product-levels.md](docs/15-product-levels.md)

---

## Out of scope (this course)

- Full auth / multi-tenant SaaS
- UI (web or mobile) — API + CLI first; UI is a fine L4 stretch
- Replacing your company’s existing deploy system — you **integrate** with it in L4

---

## Repo map

```
PRODUCT.md              ← you are here (what & why)
release-ready/          ← the product codebase
  release_ready/core/   ← L1
  release_ready/api/    ← L2
  release_ready/cli/    ← L3
  tests/                ← the contract (your eval)
exercises/              ← what to build each session
docs/                   ← how to work like an AI engineer
sample-app/             ← optional legacy SwiftUI (not the product)
```

---

## Elevator pitch (teach this in 10 seconds)

**“Release Ready is a checklist engine that tells you and your CI pipeline whether a build is allowed to ship — with tests proving every gate works.”**

Next: [docs/00-start-here.md](docs/00-start-here.md) · [release-ready/README.md](release-ready/README.md)
