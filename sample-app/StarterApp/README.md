# StarterApp (sample iOS app)

Minimal SwiftUI habit list used **only** for Cursor tutorial exercises. Open in Xcode:

```bash
open StarterApp.xcodeproj
```

Press **⌘R** — you should see **StarterApp** in the nav bar with two sample habits.

## Notes

- **iOS 17+** — `@Observable`, `#Preview`, `NavigationStack`
- **Signing:** Set your Team in Xcode → StarterApp target → Signing & Capabilities
- **Bundle ID:** `io.everytech.starterapp` (change locally if it conflicts)
- **Not a product** — in-memory data, intentional gaps for exercises (see root [AGENTS.md](../../AGENTS.md))

## Verify from terminal (optional)

```bash
xcodebuild -scheme StarterApp \
  -destination 'generic/platform=iOS Simulator' \
  build
```
