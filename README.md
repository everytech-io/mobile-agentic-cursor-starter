# Mobile → AI Engineer

**EveryTech** — transition **rusty mobile developers** into **AI engineers** who spec, engineer context, delegate to agents, verify with evidence, and ship.

[![EveryTech](https://img.shields.io/badge/org-everytech--io-blue)](https://github.com/everytech-io/mobile-agentic-cursor-starter)

## ShipGate — the training app

Build **[ShipGate](shipgate/)** (pre-ship checklist) through **four levels** — core → API → CLI → transfer. Verifiers are real from day one: `pytest`, `curl`, exit codes.

| Level | Week | Layer | Verifier |
|-------|------|-------|----------|
| **L1** | 1 | Python domain | `pytest tests/test_core.py` |
| **L2** | 2 | FastAPI REST | `pytest tests/test_api.py` + `curl` |
| **L3** | 2–3 | CLI for CI | `shipgate check` exit code |
| **L4** | 3 | Your work | Your project's tests/scripts/MCP |

Map: [docs/15-shipgate-levels.md](docs/15-shipgate-levels.md)

Optional legacy iOS sandbox: [sample-app/](sample-app/) — not required.

## Start here

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .

cd shipgate && uv venv && source .venv/bin/activate && uv pip install -e ".[dev]"
pytest -q   # 2 failures until Exercises 02–03 — expected
```

1. **[AI engineer mindset](docs/00-ai-engineer-mindset.md)**
2. **[ShipGate levels](docs/15-shipgate-levels.md)**
3. [Watch — Cursor Learn](docs/00-watch-first.md)
4. [Day 1](docs/00-start-here.md)

**Syllabus:** [docs/07-week-1-syllabus.md](docs/07-week-1-syllabus.md)

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

| Layer | Tools |
|-------|--------|
| Context | AGENTS.md, skills, `@`, LEARNINGS, plans in git |
| Delegate | Ask / Agent / Plan / Debug, MCP (Week 3+) |
| Verify | `pytest`, `curl`, scripts — parallel human + Bugbot |

Deep dive: [14-verification-practices.md](docs/14-verification-practices.md) · [05-verify-loop.md](docs/05-verify-loop.md)

## Docs map

| Topic | Doc |
|-------|-----|
| **ShipGate levels** | [15-shipgate-levels](docs/15-shipgate-levels.md) |
| Mindset | [00-ai-engineer-mindset](docs/00-ai-engineer-mindset.md) |
| Competencies | [12-ai-engineer-competencies](docs/12-ai-engineer-competencies.md) |
| Verification | [14-verification-practices](docs/14-verification-practices.md) |
| Context | [13-context-engineering](docs/13-context-engineering.md) |

## Repo layout

```
shipgate/           # Primary app — Levels 1–3
  shipgate/core/    # Level 1 domain
  shipgate/api/     # Level 2 REST
  shipgate/cli/     # Level 3 terminal
  tests/            # Your eval suite
  scripts/verify.sh # Named verifier for AGENTS.md
exercises/          # 01–09 mapped to levels
sample-app/         # Optional legacy SwiftUI sandbox
AGENTS.md           # Always-on context
.cursor/skills/     # shipgate-core, verify-after-edit
```

## License

MIT
