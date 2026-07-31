# Exercise 01 — Explore the codebase

**Goal:** Orient with Agent before writing code.  
**Time:** ~20 minutes  
**Verify:** No code changes required.

## Steps

1. Open Cursor on this repo root.
2. Open Agent (**⌘I**).
3. Paste:

```
@sample-app/StarterApp/

Explain StarterApp like I'm a rusty iOS dev returning after a break.
Include:
- App entry point
- How habits are stored (in memory? persisted?)
- Main user flows today
- File I'd open first to change the list UI
- One deliberate gap in the app meant for exercises

Max 12 bullets.
```

4. Open each file Agent mentions. Confirm paths exist — **do not trust paths you haven't clicked**.
5. In Xcode, run the app (**⌘R**). Match Agent's description to what you see.

## Success criteria

- [ ] You can name the entry `@main` file
- [ ] You found `HabitListView` (or equivalent list view)
- [ ] You ran the app once in Xcode
- [ ] You noticed the empty list is rough (setup for Exercise 02)

## Reflect (2 sentences in LEARNINGS.md)

What did Agent get right? What was wrong or vague?

Next: [02-small-change.md](02-small-change.md)
