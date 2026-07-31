# HabitPeek sample app

Minimal SwiftUI app for Cursor exercises. Open in Xcode:

```bash
open StarterApp.xcodeproj
```

## Notes

- **iOS 17+** — uses `@Observable` and `#Preview`
- **Signing:** Select your Team in Xcode → StarterApp target → Signing & Capabilities
- **Bundle ID:** `io.everytech.habitpeek` (change if it conflicts locally)

## Verify from terminal (optional)

```bash
xcodebuild -scheme StarterApp \
  -destination 'platform=iOS Simulator,name=iPhone 16' \
  build
```

Intentional gaps for learners are documented in the root [AGENTS.md](../../AGENTS.md).
