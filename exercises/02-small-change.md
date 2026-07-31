# Exercise 02 — Small verified change

**Goal:** One Agent edit, **parallel verify**.  
**Time:** ~30–45 minutes  
**Read first:** [docs/02-day-1-explore-and-edit.md](../docs/02-day-1-explore-and-edit.md), [docs/05-verify-loop.md](../docs/05-verify-loop.md)

## Spec (paste into Agent first)

```
## Goal
When StarterApp has zero habits, show a friendly empty state with title and subtitle instead of a blank list.

## Done when
- [ ] Sandbox build succeeds (`xcodebuild` or your chosen verifier — name the command)
- [ ] Manual path: deleting all habits shows the empty state
- [ ] Human: diff reviewed — only SwiftUI files under sample-app/ changed
- [ ] Agent review: `/review-bugbot` run on sample-app (parallel with build)

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

## Verify (parallel lanes)

Start all at once when the diff is ready:

1. **Automated:** `xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build` (or sandbox verifier you named)
2. **Human:** read diff; run manual empty-state path
3. **Agent review:** `/review-bugbot` on `sample-app/`

## If build fails

Paste full verifier output. Ask for minimal fix only.

## Capture

Append to [LEARNINGS.md](../LEARNINGS.md):

```markdown
## YYYY-MM-DD — Exercise 02 empty state
- Worked:
- Failed:
- Rule for next time:
```

Next: [03-plan-feature.md](03-plan-feature.md)
