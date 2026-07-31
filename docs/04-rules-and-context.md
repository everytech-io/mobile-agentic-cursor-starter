# Rules and context

Agents forget between sessions. **Rules and LEARNINGS.md are your memory.**

Official: [Rules](https://cursor.com/docs/rules) · [Context / @ mentions](https://cursor.com/help/customization/context.md)

## Three layers in this repo

| Layer | File | Purpose |
|-------|------|---------|
| Project instructions | [AGENTS.md](../AGENTS.md) | Always-on project context |
| Path-scoped rules | [.cursor/rules/swiftui-exercises.mdc](../.cursor/rules/swiftui-exercises.mdc) | SwiftUI conventions for `sample-app/` |
| Your session log | [LEARNINGS.md](../LEARNINGS.md) | What worked / failed for you |

## Using @ context

In Agent chat, type `@` to attach:

- `@HabitListView.swift` — one file
- `@sample-app/StarterApp/StarterApp/` — a folder
- `@swiftui-exercises` — a rule (if configured in picker)

**Mobile habit:** Pin the files you care about. Do not let Agent grep randomly on a large codebase.

## When to add a new rule

Add a rule only when Agent makes the **same mistake twice**.

Example: keeps using `NavigationView` → add to `.cursor/rules/`:

```markdown
Never use NavigationView or NavigationLink(destination:). Use NavigationStack + navigationDestination.
```

Official best practice: [Rules — start simple](https://cursor.com/docs/rules#best-practices)

## Exercise

Do [04-capture-learning.md](../exercises/04-capture-learning.md) after your next session.

Next: [06-cursor-plus-xcode.md](06-cursor-plus-xcode.md)
