# Debug Mode and review (Bugbot)

## Debug Mode

Official: [Debug Mode](https://cursor.com/docs/agent/debug-mode)

Debug Mode is for bugs where **reading code is not enough** — you need runtime evidence.

### Flow

1. **Hypothesize** — agent explores code, lists possible causes
2. **Instrument** — adds logging (Cursor debug extension captures runtime)
3. **You reproduce** — follow agent steps in simulator
4. **Analyze logs** — agent reads evidence
5. **Targeted fix** — small diff, not a rewrite
6. **Verify + cleanup** — confirm fix; agent removes instrumentation

### Switch to Debug Mode

Mode picker → **Debug**, or **Shift+Tab** until Debug.

### iOS + Debug Mode notes

- Reproduction happens in **Xcode simulator** (⌘R)
- Paste **Xcode console output** if Debug instrumentation is limited for SwiftUI
- For compile errors, skip Debug — paste build error into Agent

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

## Agent Review and Bugbot

Official: [Agent review](https://cursor.com/docs/agent/agent-review) · [Bugbot](https://cursor.com/docs/bugbot)

**Review is not implementation** — it is a gate before you trust the diff.

### When to review

- After Exercise 02–03 before marking done
- Before opening a PR on your real app
- After Plan Mode build completes

### `/review-bugbot`

In Agent chat:

```
/review-bugbot

Review uncommitted changes under sample-app/.
Look for: SwiftUI state bugs, missing @MainActor, NavigationStack mistakes, delete/add edge cases.
List findings by severity. Do not fix unless I ask.
```

### Manual review checklist (mobile)

- [ ] Diff only touches expected files
- [ ] No `NavigationView` / `ObservableObject` slipped in
- [ ] Xcode ⌘B clean
- [ ] Manual test path from exercise spec
- [ ] LEARNINGS.md updated

### Debug vs Bugbot

| | Debug Mode | Bugbot / review |
|---|------------|-----------------|
| Goal | Find root cause of repro bug | Find defects in written code |
| You do | Reproduce bug | Read findings |
| Output | Fix + cleanup | Report (optional fixes) |

Next: [08-cursor-modes.md](08-cursor-modes.md) (mode map) · [Exercise 08](../exercises/08-full-loop.md)
