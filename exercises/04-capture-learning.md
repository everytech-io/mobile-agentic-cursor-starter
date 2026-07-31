# Exercise 04 — Capture learning + add a rule

**Goal:** Make the workflow durable across sessions.  
**Time:** ~45 minutes  
**Read first:** [docs/04-rules-and-context.md](../docs/04-rules-and-context.md)

## Part A — LEARNINGS audit

1. Open [LEARNINGS.md](../LEARNINGS.md)
2. Ensure you have at least **2 dated entries** from exercises 01–03
3. Add a third entry summarizing your biggest surprise so far

Template:

```markdown
## YYYY-MM-DD — Week 1 reflection
- Biggest surprise about Agent:
- Biggest surprise about Xcode verify:
- One thing I'll always do from now on:
```

## Part B — Add one project rule

Pick **one** mistake Agent made twice (or might make on your team app).

Examples:

- Deprecated navigation APIs
- Wrong deployment target APIs
- Adding packages without asking

Create or extend `.cursor/rules/swiftui-exercises.mdc` with one bullet.

Or ask Agent:

```
/create-rule

When editing SwiftUI in sample-app/, never use NavigationView or ObservableObject.
Always state iOS 17 minimum.
```

Review the generated rule before committing.

## Part C — Optional commit

If you're learning git + Agent:

```
Stage only LEARNINGS.md and .cursor/rules/. Write a one-line commit message. Do not push.
```

(Mentor pushes; learners practice locally.)

## Done when

- [ ] LEARNINGS.md has 3+ entries
- [ ] At least one custom rule bullet exists
- [ ] You can explain why rules beat re-prompting every session

Course complete for Week 1 core — see [docs/07-week-1-syllabus.md](../docs/07-week-1-syllabus.md).
