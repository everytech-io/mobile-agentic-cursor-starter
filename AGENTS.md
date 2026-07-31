# Project instructions for Cursor Agent

Learner is building **Release Ready** — see [PRODUCT.md](PRODUCT.md).

**One line:** checklist engine that answers *can we ship?* with tests, API, and CLI.

## Loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

## Product codebase

- **Root:** `release-ready/`
- **L1 domain:** `release_ready/core/`
- **L2 API:** `release_ready/api/`
- **L3 CLI:** `release_ready/cli/` → command `release-ready`
- **Verifier:** `cd release-ready && ./scripts/verify.sh`

## Exercise gaps (do not fix unless exercise says)

| Gap | Ex |
|-----|-----|
| `empty_message()` blank | 02 |
| `get_item_detail()` + GET item route | 03 |
| FAILED toggle bug | 05 |

## Rules

1. Read [PRODUCT.md](PRODUCT.md) and current `exercises/` before large edits.
2. Minimal diffs — one exercise at a time.
3. After edits: parallel verify (pytest, human diff, `/review-bugbot` on `release-ready/`).

## Skills

- `.cursor/skills/release-ready-core/`
- `.cursor/skills/verify-after-edit/`

Optional legacy iOS: `sample-app/` — not the product.
