# Exercise 07 — Create a skill

**Goal:** Author a reusable skill with `/create-skill`.  
**Time:** ~45 min  
**Read first:** [docs/10-skills.md](../docs/10-skills.md)

## Task

Create **`ios-verify`** skill scoped to the sample app:

```
/create-skill

Name: ios-verify
Description: Run after editing StarterApp Swift files. Walks through Xcode verify and LEARNINGS capture.
Paths: sample-app/**/*.swift

Steps for agent:
1. Summarize files changed
2. Remind learner: Xcode ⌘B then ⌘R
3. If build fails, ask for pasted Xcode error before more edits
4. Remind to append LEARNINGS.md
5. Offer /review-bugbot on sample-app changes
```

## Review before commit

- [ ] `.cursor/skills/ios-verify/SKILL.md` exists
- [ ] `name` matches folder
- [ ] `description` says when to use it
- [ ] `paths` scopes to sample-app

## Test

New Agent chat:

```
/swiftui-exercises
/ios-verify

I just finished editing HabitListView. What's next?
```

## Done when

- [ ] Skill invokes correctly
- [ ] Committed to git (optional: PR to everytech-io repo if forking)

Next: [08-full-loop.md](08-full-loop.md)
