#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
elif command -v uv >/dev/null 2>&1; then
  exec uv run pytest -q "$@"
fi

echo "== Release Ready verify =="
python -m pytest -q "$@"
