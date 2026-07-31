# Exercise 05 — Debug Mode

**Goal:** Use Debug Mode for a reproducible logic bug.  
**Time:** ~60 min  
**Read first:** [docs/11-debug-and-review.md](../docs/11-debug-and-review.md)

## Setup

Complete Exercise 02 (empty state) first if you haven't — Debug works best on real UI state.

## Spec

```
Debug Mode:

Bug: When I delete ALL habits then add one new habit, the list sometimes looks wrong
(empty or stale) until I background the app.

Repro:
1. ⌘R StarterApp
2. Swipe-delete every habit
3. Add → "Morning run" → Save
4. Observe list

Expected: one row "Morning run"
Actual: (describe what you see)

@HabitListView.swift @HabitStore.swift

Hypothesize, instrument if useful, fix minimally, verify in Xcode, remove debug logs.
```

## Steps

1. **Shift+Tab** → **Debug** mode
2. Paste spec above (edit Actual after you reproduce)
3. Follow agent reproduction steps in simulator
4. **⌘R** after fix — repeat repro path
5. Confirm instrumentation removed from diff

## If Debug Mode is limited for SwiftUI

Fallback workflow (still valid):

1. Ask mode: trace state flow for empty → add
2. Paste **Xcode console** output into Debug/Agent chat
3. Minimal fix + verify

## Capture

LEARNINGS entry: Did Debug beat guess-and-check?

Next: [06-agents-md.md](06-agents-md.md)
