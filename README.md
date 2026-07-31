# Mobile → AI Engineer

**EveryTech** — transition **rusty mobile developers** into **AI engineers** who spec, engineer context, delegate to agents, verify with evidence, and ship.

## The product you build: Release Ready

**Can we ship this build?** A checklist engine with tests, API, and CLI — the same “gates before TestFlight/deploy” idea you already know, as a real product.

| | |
|---|---|
| **What** | [PRODUCT.md](PRODUCT.md) — read this first |
| **Code** | [release-ready/](release-ready/) |
| **Levels** | [docs/15-product-levels.md](docs/15-product-levels.md) |

| Level | Week | You add | Verifier |
|-------|------|---------|----------|
| **L1** | 1 | Core logic | `pytest tests/test_core.py` |
| **L2** | 2 | REST API | `pytest tests/test_api.py` + `curl` |
| **L3** | 2–3 | CLI for CI | `release-ready check` exit code |
| **L4** | 3 | Your stack / persistence | your tests + MCP |

## Start

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .

# Read the product
open PRODUCT.md

cd release-ready && uv venv && source .venv/bin/activate && uv pip install -e ".[dev]"
pytest -q   # 2 failures until Ex 02–03 — expected
```

1. [PRODUCT.md](PRODUCT.md)
2. [AI engineer mindset](docs/00-ai-engineer-mindset.md)
3. [Day 1](docs/00-start-here.md)

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

## Repo layout

```
PRODUCT.md           ← what you're building (start here)
release-ready/       ← the product
exercises/           ← leveled tasks
docs/                ← how to work with agents
sample-app/          ← optional legacy SwiftUI (not the product)
```

MIT
