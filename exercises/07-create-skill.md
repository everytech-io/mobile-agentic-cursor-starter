# Exercise 07 — Create a skill

**Goal:** Author a reusable skill with `/create-skill`.  
**Time:** ~45 min  
**Read first:** [docs/10-skills.md](../docs/10-skills.md)

## Task

Create **`verify-after-edit`** skill (or extend the repo example):

```
/create-skill

Name: verify-after-edit
Description: After agent edits, run parallel verification — automated verifier, human diff review, agent review.
Paths: sample-app/**/*.swift  (or omit paths for project-wide)

Steps for agent:
1. Summarize files changed
2. Lane 1 — remind learner to run named automated verifier from done-when
3. Lane 2 — human reads diff + manual path
4. Lane 3 — offer /review-bugbot in parallel (do not wait for lane 1)
5. On failure, ask for full verifier output before more edits
6. Remind LEARNINGS.md
```

Reference: [.cursor/skills/verify-after-edit/SKILL.md](../.cursor/skills/verify-after-edit/SKILL.md)

## Review before commit

- [ ] `.cursor/skills/verify-after-edit/SKILL.md` exists (or your variant)
- [ ] `name` matches folder
- [ ] `description` says when to use it
- [ ] Skill encodes **parallel** lanes, not "Xcode only"

## Test

New Agent chat:

```
/verify-after-edit

I just finished editing HabitListView. What's next?
```

## Done when

- [ ] Skill invokes correctly
- [ ] Mentions parallel human + agent review
- [ ] Committed to git (optional: PR to everytech-io repo if forking)

Next: [08-full-loop.md](08-full-loop.md)
