# Verification practices (AI engineer)

What you actually teach in the agentic era — not "open Xcode and pray."

---

## Principle 1: Done-when is the eval

The spec's **done-when** list *is* your test plan. Every item must map to at least one verifier:

| Done-when item | Verifier |
|----------------|----------|
| "API returns 404 for missing id" | `curl` + assert status |
| "Script exits 0 on happy path" | run script, check `$?` |
| "Empty list shows message" | manual path or UI test |
| "No new lint warnings" | `eslint` / `swiftlint` / `ruff` |

If you cannot name the verifier, the spec is not ready to delegate.

---

## Principle 2: Three lanes, parallel

After delegate produces a diff:

1. **Automated** — tests, build, lint, curl, scripts
2. **Human** — read diff + walk done-when path
3. **Agent review** — Bugbot or review prompt on the diff

Start all three without waiting. See [05-verify-loop.md](05-verify-loop.md).

```
Human diff review  ──┐
Agent review       ──┼──► merge findings → mark done
Automated checks   ──┘
```

---

## Principle 3: Verifier follows the work, not the IDE

| Work type | Typical verifiers | Not the default |
|-----------|-------------------|-----------------|
| Backend / API | unit tests, integration tests, curl | — |
| Scripts / data | exit code, snapshot diff, dry-run | — |
| Docs / specs | peer read, checklist, link check | — |
| Tickets | branch CI, staging smoke, PR template | — |
| iOS sandbox (this course, Ex 01–08) | `xcodebuild` or simulator | **Not graduation standard** |

**Graduation ([Exercise 09](../exercises/09-ai-engineer-graduation.md)):** verifier must match *your* real task — not "I ran the simulator."

---

## Principle 4: Evidence in chat and git

Paste verifier output into Agent when fixing failures. Append LEARNINGS when the agent repeats a mistake.

Evidence types that count:

- Command + exit code + relevant stdout/stderr
- Test name that failed / passed
- PR link with green checks
- Screenshot or log snippet for manual paths (when no automation exists)

---

## Principle 5: Review ≠ verify, but both gate ship

| | Verify | Review |
|---|--------|--------|
| Question | "Does it meet done-when?" | "What defects are in this diff?" |
| Who | You + automated + (optional) runtime | You + review agent |
| When | Parallel after diff | Parallel after diff |
| Blocks done? | Yes | Yes — triage findings |

Neither lane alone is enough.

---

## Teaching sequence (facilitator)

| Week | Emphasize |
|------|-----------|
| 1 | Done-when + human diff review + one automated command |
| 2 | Add parallel Bugbot; Debug Mode for runtime bugs |
| 3 | Learner picks verifiers for real project; no Xcode requirement |

---

## Quick rubric

**Level 1:** names done-when; runs at least one automated verifier; reads diff.

**Level 2:** runs human + agent review in parallel; pastes errors back with evidence.

**Level 3:** designs verifier set for non-mobile work; documents verify ritual in AGENTS.md or skill.

Next: [05-verify-loop.md](05-verify-loop.md) · [12-ai-engineer-competencies.md](12-ai-engineer-competencies.md)
