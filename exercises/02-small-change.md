# Exercise 02 — Small verified change

**Goal:** One Agent edit, verified in Xcode.  
**Time:** ~30–45 minutes  
**Read first:** [docs/02-day-1-explore-and-edit.md](../docs/02-day-1-explore-and-edit.md)

## Spec (paste into Agent first)

```
## Goal
When HabitPeek has zero habits, show a friendly empty state with title and subtitle instead of a blank list.

## Done when
- [ ] Xcode ⌘B succeeds
- [ ] Xcode ⌘R — deleting all habits shows the empty state
- [ ] Copy is clear for a habit tracker app
- [ ] Only SwiftUI files under sample-app/StarterApp/ changed

## Out of scope
- Core Data / SwiftData
- New screens
- Design system / assets overhaul
```

## Implementation prompt (after spec)

```
Implement the spec above.
Use iOS 17 APIs. Match existing code style.
@HabitListView.swift @HabitStore.swift
```

Adjust `@` paths to match actual filenames if needed.

## Verify

1. **⌘B** in Xcode
2. **⌘R** — add habits, delete all, confirm empty state
3. Review diff — reject unrelated files

## If build fails

Paste full Xcode error. Ask for minimal fix only.

## Capture

Append to [LEARNINGS.md](../LEARNINGS.md):

```markdown
## YYYY-MM-DD — Exercise 02 empty state
- Worked:
- Failed:
- Rule for next time:
```

Next: [03-plan-feature.md](03-plan-feature.md) (after [docs/05-verify-loop.md](../docs/05-verify-loop.md))
