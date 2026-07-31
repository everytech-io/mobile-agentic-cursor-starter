import Foundation

struct Habit: Identifiable, Hashable {
    let id: UUID
    var title: String
    var streak: Int
    let createdAt: Date

    init(id: UUID = UUID(), title: String, streak: Int = 0, createdAt: Date = .now) {
        self.id = id
        self.title = title
        self.streak = streak
        self.createdAt = createdAt
    }
}
