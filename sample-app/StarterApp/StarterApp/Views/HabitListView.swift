import SwiftUI

struct HabitListView: View {
    @Environment(HabitStore.self) private var store
    @State private var newHabitTitle = ""
    @State private var isAdding = false

    var body: some View {
        NavigationStack {
            List {
                ForEach(store.habits) { habit in
                    HabitRow(habit: habit)
                }
                .onDelete(perform: store.delete)
            }
            .navigationTitle("HabitPeek")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Add") { isAdding = true }
                }
            }
            .alert("New habit", isPresented: $isAdding) {
                TextField("Title", text: $newHabitTitle)
                Button("Cancel", role: .cancel) { newHabitTitle = "" }
                Button("Save") {
                    store.addHabit(title: newHabitTitle)
                    newHabitTitle = ""
                }
            } message: {
                Text("What do you want to track?")
            }
        }
    }
}

private struct HabitRow: View {
    let habit: Habit

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(habit.title)
                .font(.headline)
            Text("Streak: \(habit.streak) day\(habit.streak == 1 ? "" : "s")")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding(.vertical, 4)
    }
}

#Preview {
    HabitListView()
        .environment(HabitStore())
}
