import Foundation
import Observation

@Observable
final class HabitStore {
    var habits: [Habit]

    init(habits: [Habit] = HabitStore.sampleHabits) {
        self.habits = habits
    }

    func addHabit(title: String) {
        let trimmed = title.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { return }
        habits.append(Habit(title: trimmed))
    }

    func delete(at offsets: IndexSet) {
        habits.remove(atOffsets: offsets)
    }

    private static let sampleHabits: [Habit] = [
        Habit(title: "Morning walk", streak: 3, createdAt: .now.addingTimeInterval(-86400 * 5)),
        Habit(title: "Read 10 pages", streak: 1, createdAt: .now.addingTimeInterval(-86400 * 2)),
    ]
}
