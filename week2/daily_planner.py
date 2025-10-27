
import datetime

def create_daily_plan():
    print("=== Daily Planner ===")
    try:
        num_tasks = int(input("How many tasks do you want to plan today? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    tasks = []

    for i in range(num_tasks):
        print(f"\nTask {i + 1}:")
        name = input("Task name: ").strip().title()
        priority = input("Priority (High/Medium/Low): ").capitalize()
        time_slot = input("Time slot (e.g., 9AM–10AM): ").strip()

        task = {
            "name": name,
            "priority": priority,
            "time_slot": time_slot
        }
        tasks.append(task)

    print("\n--- Your Plan for Today ---")
    for task in tasks:
        symbol = "🕘"
        if task["priority"] == "High":
            symbol = "🔥"
        elif task["priority"] == "Medium":
            symbol = "⚙️"
        elif task["priority"] == "Low":
            symbol = "🌙"

        print(f"{symbol} {task['time_slot']} → {task['name']} [{task['priority'].upper()}]")

    # Optional: Save to file
    save = input("\nWould you like to save this plan to a file? (y/n): ").lower()
    if save == 'y':
        today = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"daily_plan_{today}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== Daily Planner ({today}) ===\n")
            for task in tasks:
                f.write(f"{task['time_slot']} → {task['name']} [{task['priority']}]\n")
        print(f"✅ Plan saved to {filename}")
    else:
        print("📝 Plan not saved, exiting...")

if __name__ == "__main__":
    create_daily_plan()
