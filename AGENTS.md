# Project instructions for Cursor Agent

You are helping a **rusty mobile developer** learn agentic workflow in this tutorial repo.

## Stack

- **Sample app:** HabitPeek — SwiftUI, iOS 17+, `@Observable`, `NavigationStack`
- **Path:** `sample-app/StarterApp/StarterApp/`
- **Verify:** Learner must build/run in **Xcode** after edits. Remind them if they skip verify.

## Workflow rules

1. Read the relevant exercise in `exercises/` before large changes.
2. Prefer minimal diffs — one exercise scope at a time.
3. Never add Swift packages unless the exercise asks.
4. Never use `NavigationView`, `ObservableObject`, or `@Published` in new code.
5. After editing, suggest: Xcode ⌘B, ⌘R, and a LEARNINGS.md entry.

## Repo layout

- `docs/` — guided reading (ordered)
- `exercises/` — hands-on prompts
- `LEARNINGS.md` — learner session log (append only)
- `.cursor/skills/swiftui-exercises/` — SwiftUI conventions (loads when editing sample-app)

## Intentional gaps (for exercises)

- Empty list has no dedicated empty state (Exercise 02)
- Rows are not tappable / no detail screen (Exercise 03)
- In-memory storage only — no persistence

Do not "fix" these unless the current exercise requires it.
