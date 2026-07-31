# Debug Mode and review (Bugbot)

## Debug Mode

Official: [Debug Mode](https://cursor.com/docs/agent/debug-mode)

Debug Mode is for bugs where **reading code is not enough** — you need runtime evidence.

### Flow

1. **Hypothesize** — agent explores code, lists possible causes
2. **Instrument** — adds logging (Cursor debug extension captures runtime)
3. **You reproduce** — follow agent steps (simulator, server, script — whatever your task uses)
4. **Analyze logs** — agent reads evidence
5. **Targeted fix** — small diff, not a rewrite
6. **Verify + cleanup** — confirm fix; agent removes instrumentation

### Switch to Debug Mode

Mode picker → **Debug**, or **Shift+Tab** until Debug.

### Sandbox notes (StarterApp)

- Reproduction may use simulator or `xcodebuild` — optional for this course
- Paste **runtime log output** if instrumentation is limited
- For compile errors, skip Debug — paste build/test output into Agent

### Good Debug prompt

```
Debug Mode:

Bug: After deleting the last habit, adding a new one sometimes shows a blank row until I navigate away.

Repro:
1. Launch StarterApp
2. Delete all habits (swipe)
3. Tap Add → save "Test"
4. Sometimes row is empty

Expected: new habit title visible immediately.
@HabitListView.swift @HabitStore.swift
```

See [Exercise 05](../exercises/05-debug-mode.md).

---

## Agent Review and Bugbot (parallel lane)

Official: [Agent review](https://cursor.com/docs/agent/agent-review) · [Bugbot](https://cursor.com/docs/bugbot)

**Review runs in parallel with verify** — start when the diff exists, not after all manual tests finish.

### When to review

- As soon as Agent/Plan produces a diff
- Before opening a PR on your real app
- Same session as automated tests and human diff read

### `/review-bugbot`

In Agent chat (while tests run or you read the diff):

```
/review-bugbot

Review uncommitted changes under sample-app/.
Look for: SwiftUI state bugs, missing @MainActor, NavigationStack mistakes, delete/add edge cases.
List findings by severity. Do not fix unless I ask.
```

### Parallel checklist (all lanes)

| Lane | Check |
|------|-------|
| **Human** | Diff only touches expected files; manual done-when path |
| **Automated** | Named verifier green (test / build / lint — paste output if red) |
| **Agent review** | Bugbot findings triaged |
| **Capture** | LEARNINGS.md updated |

### Debug vs Bugbot

| | Debug Mode | Bugbot / review |
|---|------------|-----------------|
| Goal | Find root cause of repro bug | Find defects in written code |
| You do | Reproduce bug | Read findings (parallel with other verify) |
| Output | Fix + cleanup | Report (optional fixes) |

Next: [14-verification-practices.md](14-verification-practices.md) · [08-cursor-modes.md](08-cursor-modes.md)
