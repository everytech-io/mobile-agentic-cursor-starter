---
name: verify-after-edit
description: After agent edits, run parallel verification — automated verifier, human diff review, and agent review. Use when changes are complete or learner asks what to do before marking done.
paths: shipgate/**/*
---

# Verify after edit (parallel lanes)

Run after any agent edit batch.

## Three lanes (parallel — start all at once)

1. **Automated** — `cd shipgate && ./scripts/verify.sh` or pytest subset from done-when
2. **Human** — learner reads diff; walks manual path from spec
3. **Agent review** — `/review-bugbot` on `shipgate/` — do not wait for pytest to finish

## On failure

Ask for **full pytest/curl output** before more edits.

## Close

Append [LEARNINGS.md](../../LEARNINGS.md). Mark done only when done-when checklist is green.
