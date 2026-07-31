# Start here

Read **[00-ai-engineer-mindset.md](00-ai-engineer-mindset.md)** then **[15-release-ready-levels.md](15-release-ready-levels.md)**.

## One workspace: Release Ready

| Tool | Role |
|------|------|
| **Cursor** | Spec, context, delegate, parallel verify + review |
| **pytest / curl** | Automated verifiers from Level 1 |

No Xcode required. Optional iOS sandbox: [sample-app/](../sample-app/).

## Before you begin

- [ ] [AI engineer mindset](00-ai-engineer-mindset.md)
- [ ] [Release Ready levels](15-release-ready-levels.md)
- [ ] [Competency map](12-ai-engineer-competencies.md)
- [ ] [Watch Cursor Learn](00-watch-first.md)
- [ ] Release Ready setup:

```bash
cd release-ready && uv venv && source .venv/bin/activate && uv pip install -e ".[dev]"
pytest -q   # 2 failures until Ex 02–03 — expected
```

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

## Day 1

| Step | Link | Time |
|------|------|------|
| 1 | [01-install-and-open.md](01-install-and-open.md) | 15 min |
| 2 | [Exercise 01](../exercises/01-explore.md) | 20 min |
| 3 | [02-day-1-explore-and-edit.md](02-day-1-explore-and-edit.md) | 15 min |
| 4 | [Exercise 02](../exercises/02-small-change.md) | 30 min |

Next: [01-install-and-open.md](01-install-and-open.md)
