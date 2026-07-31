---
name: swiftui-exercises
description: SwiftUI conventions for the sample habit-tracker app under sample-app/. Use when editing Swift files in exercises.
paths: sample-app/**/*.swift
---

# SwiftUI exercise conventions

- Minimum deployment target: **iOS 17**. Use `@Observable`, `#Preview`, and `NavigationStack`.
- Never use `NavigationView`, `ObservableObject`, or `@Published` in new code.
- Keep views under ~150 lines; extract subviews when needed.
- No third-party packages unless the exercise asks.
- After edits, remind **parallel verify**: named automated command + human diff + `/review-bugbot` ([05-verify-loop.md](../../docs/05-verify-loop.md)).
