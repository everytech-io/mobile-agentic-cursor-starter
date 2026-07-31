# Exercise 03 — Plan Mode feature

**Goal:** Multi-file feature with plan approval before code.  
**Time:** ~90 minutes  
**Read first:** [docs/03-plan-mode.md](../docs/03-plan-mode.md)

## Spec

```
Plan Mode: Add a habit detail screen to HabitPeek.

## Done when
- [ ] Tap habit row → detail screen with title, streak, created date
- [ ] Back navigation works (NavigationStack)
- [ ] Xcode ⌘B / ⌘R pass
- [ ] iOS 17+, @Observable HabitStore, no new dependencies

## Out of scope
- Edit/delete on detail screen
- Persistence
```

## Steps

1. **Shift+Tab** → Plan Mode in Agent
2. Paste spec
3. Answer Agent questions (keep scope tight)
4. Review plan — edit if it adds unnecessary architecture
5. Approve build
6. Verify in Xcode: tap each habit, back, rotate if you care about layout

## Common failures

| Symptom | Fix |
|---------|-----|
| `NavigationView` in diff | Reject; cite `/swiftui-exercises` skill or AGENTS.md |
| New files outside `Views/` | Ask to colocate with existing structure |
| Plan adds ViewModel you don't need | Shrink plan — list screen may not need one |

## Capture

LEARNINGS entry: Was Plan Mode faster than prompt-fixing? Why?

Next: [04-capture-learning.md](04-capture-learning.md)
