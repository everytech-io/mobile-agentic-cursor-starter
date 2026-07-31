# Install and open

## 1. Install Cursor

[cursor.com/downloads](https://cursor.com/downloads) — sign in.

## 2. Clone and open

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .
```

## 3. ShipGate setup (primary app)

Requires **Python 3.9+**. Recommended: [uv](https://docs.astral.sh/uv/).

```bash
cd shipgate
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest -q
```

**Expected:** 2 tests fail until Exercises 02–03. That is the red-green starting line.

Without uv:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## 4. Agent shortcuts

| Action | Mac |
|--------|-----|
| Agent | **⌘I** |
| `@` file | in chat |
| Plan Mode | **Shift+Tab** |

## 5. Named verifier (memorize)

```bash
cd shipgate && ./scripts/verify.sh
```

Add this to AGENTS.md in Exercise 06.

## Checklist

- [ ] Cursor opens repo root
- [ ] `pytest -q` runs (2 known failures OK)
- [ ] You read [15-shipgate-levels.md](15-shipgate-levels.md)

Next: [Exercise 01](../exercises/01-explore.md)
