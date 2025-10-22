import json
import datetime
from pathlib import Path

# Path to tasks.json
TASKS_FILE = Path(__file__).parent / "tasks.json"

def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("\n🟡 No tasks found.\n")
        return
    print("\n📋 Current Tasks:")
    for i, task in enumerate(tasks, start=1):
        due_raw = task.get("due_date")
        if due_raw:
            try:
                due_date = datetime.datetime.strptime(due_raw, "%Y-%m-%d").date()
                today = datetime.date.today()
                days_left = (due_date - today).days
                if days_left < 0:
                    due = f"{due_raw} (⏰ {abs(days_left)} days overdue)"
                elif days_left == 0:
                    due = f"{due_raw} (🚨 due today)"
                else:
                    due = f"{due_raw} ({days_left} days left)"
            except ValueError:
                due = f"{due_raw} (invalid date)"
        else:
            due = "N/A"
        priority = task.get("priority", "none").capitalize()
        status = "✅" if task.get("done") else "🔸"
        print(f"{i}. {status} {task['title']} | Priority: {priority} | Due: {due}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    priority = input("Priority (low/medium/high): ").lower()
    due_date = input("Due date (YYYY-MM-DD or leave blank): ").strip()
    task = {
        "title": title,
        "priority": priority if priority in ["low", "medium", "high"] else "low",
        "due_date": due_date if due_date else None,
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("🎯 Task marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        deleted = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {deleted['title']}")
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")

def search_tasks(tasks):
    if not tasks:
        print("No tasks available to search.")
        return

    print("\n🔎 Search/Filter Options:")
    print("1. By keyword")
    print("2. Filter By priority (low/medium/high)")
    choice = input("Choose filter type: ").strip()

    if choice == "1":
        term = input("Enter keyword: ").lower()
        filtered = [t for t in tasks if term in t["title"].lower()]
    elif choice == "2":
        level = input("Enter priority: ").lower()
        filtered = [t for t in tasks if t.get("priority") == level]
    else:
        print("⚠️ Invalid choice.")
        return

    if not filtered:
        print("No matches found.")
    else:
        list_tasks(filtered)


def main():
    tasks = load_tasks()
    while True:
        print("""
=== 🧠 To-Do CLI v2 ===
1. View Tasks
2. Add Task
3. Mark Task Done
4. Delete Task
5. Search / Filter Tasks
6. Exit
""")
        choice = input("Select option: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    main()
