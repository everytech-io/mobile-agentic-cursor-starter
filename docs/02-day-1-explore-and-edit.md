# Day 1: Explore and edit

Today you learn the minimum viable agent loop: **orient → one change → parallel verify**.

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
- [ ] Named build verifier green (e.g. xcodebuild — document command)
- [ ] Manual path: empty list shows helpful copy
- [ ] Human: diff reviewed
- [ ] Agent review: /review-bugbot on sample-app (parallel)

## Out of scope
- Persistence, networking, new screens
```

**Rule:** If you cannot write "done when," the Agent cannot succeed reliably.

## Part C — One small change

See [Exercise 02](../exercises/02-small-change.md) for the hands-on task.

While Agent works:

- Watch the **diff** — reject hunks you do not understand
- Do not accept "I'll fix it in a follow-up"

## Part D — Verify (parallel lanes)

After Agent finishes, start **all lanes at once**:

1. **Automated:** run the verifier you named in done-when (e.g. `xcodebuild … build`)
2. **Human:** read diff; walk manual path (empty state after delete all)
3. **Agent review:** `/review-bugbot` on `sample-app/` — do not wait for build to finish before starting this

If build fails, paste **full verifier output** into Agent:

```
Build failed:

<paste command output>

Fix only what's needed. Do not refactor unrelated files.
```

See [05-verify-loop.md](05-verify-loop.md) · [14-verification-practices.md](14-verification-practices.md).

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
| No named verifier | Write the command in done-when |
| Review only after manual test | Start Bugbot when diff exists |
| Huge first prompt | One screen, one outcome |
| Accepted diff blindly | Review like a PR |
| No LEARNINGS entry | You will repeat the same failure |

Next: [05-verify-loop.md](05-verify-loop.md) (read before Day 2)
