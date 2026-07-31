# Verify before trust

The agent is not a compiler. **Your verifiers are.**

Verification is how AI engineers stay honest. The agent optimizes for "looks done." **Done-when + evidence** is the contract.

Xcode is **not** the end goal — it is one optional verifier for the StarterApp sandbox (Exercises 01–08). Graduation and real work use **whatever proves the outcome**: tests, scripts, curl, linters, logs, PR checks, manual paths.

Official: [Reviewing and testing code](https://cursor.com/learn/reviewing-testing.md)

---

## Verification lanes (run in parallel)

After the agent produces a diff, open **three lanes at once**. Do not wait for one to finish before starting the others.

```
                    DELEGATE (diff ready)
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   AUTOMATED              HUMAN               AGENT REVIEW
   build / test           read diff           /review-bugbot
   lint / curl            manual path         review prompt
   script exit code       spot-check UX
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                         CAPTURE (LEARNINGS)
```

| Lane | Who | Examples |
|------|-----|----------|
| **Automated** | Machine | `npm test`, `pytest`, `curl`, `swiftlint`, `xcodebuild`, CI |
| **Human** | You | Read every changed file; run the done-when path yourself |
| **Agent review** | Review agent | `/review-bugbot`, explicit review prompt on the diff |

**Parallel habit:** kick off Bugbot while you read the diff and while tests run. Merge findings into one checklist before you mark done.

Sequential only where required: you need a build artifact before runtime manual test — but **review can start on the diff immediately**.

---

## Verify stack (cheap → expensive, within automated lane)

Inside the **automated** lane, prefer cheap checks first:

```
lint / typecheck → unit tests → integration → manual runtime
```

Do not ask the agent to refactor until cheap checks are green — same discipline as CI.

---

## Human lane (non-negotiable)

Even with tests and Bugbot:

1. **Read the diff** — reject drive-by refactors; ask "why this file?"
2. **Exercise the done-when path** — the scenario your spec named
3. **Domain gate** — wrong API, wrong env, wrong business rule? You catch it; agents won't

---

## Agent review lane (parallel, not a substitute)

Review agents catch patterns you might miss. They do **not** replace human judgment or automated tests.

```
/review-bugbot

Review uncommitted changes under <path>.
Look for: <risks from your spec>.
List findings by severity. Do not fix unless I ask.
```

See [11-debug-and-review.md](11-debug-and-review.md).

---

## Paste errors back correctly

Bad:

> it doesn't build fix it

Good:

```
Build failed in HabitListView.swift:42

'NavigationView' was deprecated in iOS 16.0

Fix using NavigationStack. iOS 17 minimum. Only this file unless required.
```

Paste **full verifier output** — test name, exit code, log snippet — not vibes.

---

## Sandbox only: StarterApp (Exercises 01–08)

If you are verifying SwiftUI sandbox edits, pick **one** automated path (not required for graduation):

```bash
cd sample-app/StarterApp
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

Or use Xcode ⌘B / ⌘R if you prefer a GUI. This teaches the **habit**, not the tool.

**Week 3+:** use your project's real verifiers. Do not default to Xcode unless you are shipping iOS.

---

## Done-when template (copy every session)

```markdown
## Done when
- [ ] Diff reviewed (human lane)
- [ ] Automated verifier green: ___ (test / script / curl / build — name the command)
- [ ] Manual path from spec exercised: ___
- [ ] Agent review run (parallel): findings addressed or accepted
- [ ] LEARNINGS.md updated
```

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| "Agent said it's done" | Show verifier output |
| Review only after manual test finishes | Start Bugbot when diff exists |
| Only Xcode for everything | Name the verifier that matches **this** task |
| Skip human diff review because Bugbot ran | Both lanes required |

Next: [11-debug-and-review.md](11-debug-and-review.md) · [13-context-engineering.md](13-context-engineering.md)
