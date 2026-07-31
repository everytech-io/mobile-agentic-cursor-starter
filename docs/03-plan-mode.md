# Plan Mode

Use Plan Mode when a task touches **more than one file** or needs design choices.

Official: [Plan Mode docs](https://cursor.com/docs/agent/plan-mode)

## When to use it

| Use Plan Mode | Skip Plan Mode |
|---------------|----------------|
| New screen + navigation | Fix a string |
| Refactor across folders | Single-view tweak |
| Unclear requirements | You've done it 10 times |

## How

1. Open Agent (**⌘I**)
2. Press **Shift+Tab** until mode shows **Plan**
3. Paste the exercise spec from [03-plan-feature.md](../exercises/03-plan-feature.md)
4. Answer clarifying questions
5. **Read the plan** — edit via chat if wrong
6. Click **Build** only when the plan matches your done-when list

## If the build goes wrong

Do not prompt-spam fixes. Revert, tighten the plan, run again.

From Cursor docs:

> Revert the changes, refine the plan to be more specific, and run it again. This is often faster than fixing an in-progress agent.

## Plan Mode prompt template

```
Plan Mode: Add a habit detail screen to StarterApp.

Requirements:
- Tap a row → detail shows title, streak count, created date
- Back navigation works
- iOS 17+, SwiftUI, @Observable HabitStore
- No new dependencies

Before coding, list files to create/change and acceptance checks.
Wait for my approval.
```

Next: [04-rules-and-context.md](04-rules-and-context.md)
