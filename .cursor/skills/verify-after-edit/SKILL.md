---
name: verify-after-edit
description: After agent edits, run parallel verification — automated verifier, human diff review, and agent review. Use when changes are complete or learner asks what to do before marking done.
---

# Verify after edit (parallel lanes)

Run after any agent edit batch, in **this repo or the learner's project**.

## Three lanes (parallel — start all at once)

1. **Automated** — name one command from done-when (test, lint, build, curl, script).
2. **Human** — learner reads diff; walks manual path from spec.
3. **Agent review** — suggest `/review-bugbot` or review prompt on changed paths.

Do not wait for lane 1 to finish before starting lane 3.

## Sandbox (StarterApp only)

If edits are under `sample-app/`, optional automated verifier:

```bash
cd sample-app/StarterApp
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

Simulator manual test is optional — habit only, not graduation standard.

## On failure

Ask for **full verifier output** (test name, exit code, log snippet) before more edits.

## Close

Remind to append [LEARNINGS.md](../../LEARNINGS.md). Mark done only when done-when checklist is green across lanes.
