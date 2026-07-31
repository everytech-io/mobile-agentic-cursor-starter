---
name: verify-after-edit
description: After Release Ready edits, run parallel verify — pytest, human diff, agent review.
paths: release-ready/**/*
---

# Verify after edit

1. **Automated:** `cd release-ready && ./scripts/verify.sh`
2. **Human:** diff + done-when path
3. **Agent:** `/review-bugbot` on `release-ready/` (parallel with pytest)

Paste full pytest output on failure. Append [LEARNINGS.md](../../LEARNINGS.md) when done.
