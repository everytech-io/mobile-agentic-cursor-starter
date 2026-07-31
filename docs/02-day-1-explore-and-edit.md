# Day 1: Explore and edit

Today you learn the minimum viable agent loop: **orient → one change → verify in Xcode**.

Official Cursor path: [Quickstart — explain codebase](https://cursor.com/docs/get-started/quickstart)

## Part A — Orient (Cursor)

Open Agent (**⌘I**). Use this prompt (copy verbatim):

```
Explain the StarterApp sample app under sample-app/StarterApp/.
List: entry point, main views, data model, and one intentional rough edge I could fix in an exercise.
Keep it under 15 bullet points.
```

Read the response. Click through at least two files it mentions.

**Why:** Agent without orientation invents architecture. Mobile devs already code-review — this is the same instinct.

## Part B — Spec before code

Before asking for edits, paste a mini-spec:

```
## Goal
Improve the empty state when there are no habits.

## Done when
- [ ] Builds in Xcode (⌘B)
- [ ] Runs on simulator (⌘R)
- [ ] Empty list shows helpful copy, not a blank screen

## Out of scope
- Persistence, networking, new screens
```

**Rule:** If you cannot write "done when," the Agent cannot succeed reliably.

## Part C — One small change

See [Exercise 02](../exercises/02-small-change.md) for the hands-on task.

While Agent works:

- Watch the **diff** — reject hunks you do not understand
- Do not accept "I'll fix it in a follow-up"

## Part D — Verify in Xcode

After Agent finishes:

1. Switch to Xcode
2. **⌘B** — build must succeed
3. **⌘R** — run; delete all habits in the app (swipe) to test empty state
4. Tap through once like a user, not like a developer

If build fails, copy the **full error** from Xcode's Issue navigator into Agent:

```
Build failed. Here is the error from Xcode:

<paste>

Fix only what's needed. Do not refactor unrelated files.
```

## Part E — Capture

Append to [LEARNINGS.md](../LEARNINGS.md):

```markdown
## YYYY-MM-DD — Empty state
- Worked:
- Failed / surprised me:
- Rule for next time:
```

## Common Day 1 mistakes

| Mistake | Fix |
|---------|-----|
| Never opened Xcode | Simulator is truth; Agent is draft |
| Huge first prompt | One screen, one outcome |
| Accepted diff blindly | Review like a PR |
| No LEARNINGS entry | You will repeat the same failure |

Next: [05-verify-loop.md](05-verify-loop.md) (read before Day 2)
