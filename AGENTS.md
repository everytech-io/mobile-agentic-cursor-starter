# Project instructions for Cursor Agent

You are helping a learner transition from **mobile developer** to **AI engineer**.

This repo uses **StarterApp** (SwiftUI) as a **training sandbox only**. The real outcome is the agentic loop on any codebase: spec → context → plan → delegate → verify ∥ review → capture.

## AI engineer loop

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY ∥ REVIEW → CAPTURE
```

VERIFY and REVIEW run **in parallel** after a diff exists: automated checks, human diff review, and agent review (e.g. Bugbot) at the same time.

## Stack (sandbox)

- **Sample app:** StarterApp — SwiftUI, iOS 17+, `@Observable`, `NavigationStack`
- **Path:** `sample-app/StarterApp/StarterApp/`
- **Sandbox verify (optional):** `xcodebuild`, simulator, or tests — teaches the habit, not the end goal. Graduation uses the learner's real verifiers.

## Workflow rules

1. Read the relevant exercise in `exercises/` before large changes.
2. Prefer minimal diffs — one exercise scope at a time.
3. Never add Swift packages unless the exercise asks.
4. Never use `NavigationView`, `ObservableObject`, or `@Published` in new code.
5. After editing, remind: **parallel verify** — (1) run named automated verifier, (2) human reads diff, (3) suggest `/review-bugbot`; then LEARNINGS.md.

## Repo layout

- `docs/` — guided reading (ordered)
- `docs/HIGH-LEVEL-PLAN.md` — program plan; planner subagents expand into `docs/plans/`
- `exercises/` — hands-on prompts
- `LEARNINGS.md` — learner session log (append only)
- `.cursor/skills/swiftui-exercises/` — SwiftUI conventions (sample-app)
- `.cursor/skills/verify-after-edit/` — post-edit parallel verify ritual

## Intentional gaps (for exercises)

- Empty list has no dedicated empty state (Exercise 02)
- Rows are not tappable / no detail screen (Exercise 03)
- In-memory storage only — no persistence

Do not "fix" these unless the current exercise requires it.
