# Cursor modes — when to use what

Official: [Agent overview](https://cursor.com/docs/agent/overview) · [Plan Mode](https://cursor.com/docs/agent/plan-mode) · [Debug Mode](https://cursor.com/docs/agent/debug-mode) · [Ask Mode](https://cursor.com/help/ai-features/ask-mode)

Switch modes: **mode picker** in Agent input, or **Shift+Tab** to rotate.

## Mode map (memorize this)

| Mode | You use it when | Agent writes code? | This course |
|------|-----------------|-------------------|-------------|
| **Ask** | Understand code, explore options, no edits yet | No | Day 1 orient |
| **Agent** | Scoped task, 1–few files, you review diffs | Yes | Day 1–2 default |
| **Plan** | Multi-file feature, unclear scope, architecture choice | After you approve plan | Day 3+ |
| **Debug** | Bug reproduces but cause unclear; need runtime evidence | Yes (instrument → fix → cleanup) | Week 2 |

**Verify runs in parallel** after every delegate step — automated + human + agent review. See [05-verify-loop.md](05-verify-loop.md).

## Ask Mode

**Purpose:** Read-only exploration. No surprise diffs.

```
@sample-app/StarterApp/

Explain how HabitStore.delete works and what happens if habits is empty.
Do not edit any files.
```

Use Ask before Agent when you do not know the codebase yet.

## Agent Mode (default)

**Purpose:** Implement a bounded change with tools (edit, terminal, search).

The four beats ([Working with agents](https://cursor.com/learn/working-with-agents)):

1. **Plan** (mental or mini-spec in prompt)
2. **Act** (edits)
3. **Verify ∥ Review** (parallel: automated + human diff + Bugbot)
4. **Hand back** (LEARNINGS)

## Plan Mode

**Purpose:** Research → clarifying questions → **reviewable plan** → build on approval.

**Shift+Tab** until Plan is selected.

See [03-plan-mode.md](03-plan-mode.md) and [Exercise 03](../exercises/03-plan-feature.md).

**Rule:** If Agent built the wrong thing, **revert and refine the plan** — do not prompt-spam fixes.

Save plans to the workspace (`Save to workspace`) so mentors and subagents can read them.

## Debug Mode

**Purpose:** Hypothesis → instrumentation → you reproduce → logs → targeted fix → cleanup.

Best for:

- Reproducible bugs with unclear cause
- Timing / async / state bugs
- "It used to work" regressions

**Not** for: typos, missing imports — use Agent + paste verifier output.

See [11-debug-and-review.md](11-debug-and-review.md) and [Exercise 05](../exercises/05-debug-mode.md).

## Agent Review / Bugbot (review, not a mode)

Before merging or marking an exercise done, run **in parallel** with your other verifiers:

```
/review-bugbot

Review my changes on this branch for bugs and regressions in the StarterApp sample.
Focus on SwiftUI lifecycle and delete/add habit flows.
```

Or use **Agent review** from the diff UI. See [11-debug-and-review.md](11-debug-and-review.md).

## Mode routing cheat sheet

```
"Where is X?" / "How does Y work?"     → Ask
"Change this one screen"               → Agent + spec
"Add screen + navigation + tests"      → Plan → Agent
"Crashes when I swipe delete twice"    → Debug
"Ship it — anything I missed?"         → /review-bugbot or Agent review
```

Next: [09-agents-md.md](09-agents-md.md)
