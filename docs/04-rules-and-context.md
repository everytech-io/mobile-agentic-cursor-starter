# Context, AGENTS.md, and skills

Agents forget between sessions. You give them memory with **files in the repo** — not by re-explaining every time.

Official: [Customizing agents](https://cursor.com/learn/customizing-agents) · [Skills](https://cursor.com/docs/skills) · [Context / @](https://cursor.com/help/customization/context.md)

## What to use in 2026 (simple version)

| Mechanism | When | This repo |
|-----------|------|-----------|
| **AGENTS.md** | Always-on project instructions | [AGENTS.md](../AGENTS.md) at repo root |
| **Skills** | Conventions loaded when relevant | [.cursor/skills/swiftui-exercises/](../.cursor/skills/swiftui-exercises/SKILL.md) |
| **LEARNINGS.md** | Your personal session log | [LEARNINGS.md](../LEARNINGS.md) |
| **@ mentions** | Pin files/folders in chat | `@HabitListView.swift`, `@sample-app/` |

### Do you still need `.cursor/rules/`?

**Not for Week 1.** Cursor is moving toward **skills** for most customization ([`/migrate-to-skills`](https://cursor.com/docs/skills#migrating-rules-and-commands-to-skills) converts old dynamic rules).

Use **rules** only when you need something **always injected** into every chat (team-wide guardrails, compliance). For SwiftUI conventions scoped to `sample-app/`, a **skill with `paths:`** is the modern equivalent — already in this repo.

**AGENTS.md** covers project-wide context without YAML frontmatter. Start there.

## Using @ context

In Agent chat, type `@` to attach:

- `@HabitListView.swift` — one file
- `@sample-app/StarterApp/StarterApp/` — a folder
- `/swiftui-exercises` — invoke the skill explicitly

**Mobile habit:** Pin the files you care about. Do not let Agent grep blindly on a large codebase.

## When to add more

Add a skill (or a LEARNINGS rule) only when Agent makes the **same mistake twice**.

Example skill addition:

```
/create-skill

When editing SwiftUI in sample-app/, never use NavigationView.
Always remind learner to run **parallel verify** after edits ([14-verification-practices.md](14-verification-practices.md)).
```

## Exercise

Do [04-capture-learning.md](../exercises/04-capture-learning.md) after your next session.

Next: [06-cursor-plus-xcode.md](06-cursor-plus-xcode.md) · Week 2: [08-cursor-modes.md](08-cursor-modes.md)
