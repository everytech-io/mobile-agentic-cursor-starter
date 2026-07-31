---
name: ios-verify
description: After editing StarterApp Swift files, walk through Xcode verify and LEARNINGS capture. Use when SwiftUI sample-app changes are complete or learner asks "what's next after edits".
paths: sample-app/**/*.swift
---

# iOS verify (StarterApp)

Run this after SwiftUI edits under `sample-app/`.

## Steps

1. Summarize which files changed and why (3 bullets max).
2. Remind the learner:
   - Xcode **⌘B** (build)
   - Xcode **⌘R** (run on simulator)
   - Test: add habit → delete → empty state if implemented
3. If build failed, ask for **full Xcode error text** before more edits.
4. Remind to append [LEARNINGS.md](../../LEARNINGS.md).
5. Offer `/review-bugbot` on `sample-app/` changes before marking done.

Do not mark the task complete until the learner confirms simulator verify.
