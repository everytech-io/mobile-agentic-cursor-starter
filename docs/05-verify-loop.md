# Verify before trust

The Agent is not a compiler. **Xcode is.**

This doc is the anti-vibe-coding core of the course.

## Verify stack (in order)

### 1. Read the diff (Cursor)

- Every changed file
- Reject drive-by refactors
- Ask "why this file?" if surprised

### 2. Build (Xcode)

**⌘B** — zero errors required.

### 3. Run (Xcode)

**⌘R** — exercise the path you changed.

### 4. Optional: SwiftLint

```bash
cd sample-app/StarterApp && swiftlint
```

Fix warnings Agent introduced before moving on.

### 5. Optional: tests

If you add ViewModel logic, add a unit test. Agent can draft tests; you assert behavior matters.

Official: [Reviewing and testing code](https://cursor.com/learn/reviewing-testing.md)

## Paste errors back correctly

Bad:

> it doesn't build fix it

Good:

```
Xcode build error in HabitListView.swift:42

'NavigationView' was deprecated in iOS 16.0

Fix using NavigationStack. iOS 17 minimum. Only this file unless required.
```

## Analyzer-first (mobile devs already know this)

Same idea as CI:

```
Cheap checks first → expensive Agent second
SwiftLint / build → then ask Agent to refactor
```

On Apple Silicon + Xcode 26.3+, [Xcode MCP](https://cursor.com/docs/integrations/xcode) can build from Cursor — still confirm in Xcode at least once while learning.

## Done-when template (copy every session)

```markdown
## Done when
- [ ] Xcode ⌘B succeeds
- [ ] Xcode ⌘R — manual test path: ___
- [ ] No new SwiftLint errors (if installed)
- [ ] LEARNINGS.md updated
```

Next: [03-plan-mode.md](03-plan-mode.md)
