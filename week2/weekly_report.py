import os
import datetime
from collections import Counter

def parse_plan_file(filename):
    """Extracts tasks and priorities from a saved daily plan file."""
    tasks = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "→" in line and "[" in line:
                parts = line.strip().split("→")
                if len(parts) == 2:
                    time_part, rest = parts
                    name, priority = rest.split("[")
                    tasks.append({
                        "time": time_part.strip(),
                        "name": name.strip(),
                        "priority": priority.replace("]", "").strip()
                    })
    return tasks


def generate_weekly_report():
    print("=== Weekly Report Summary ===")

    # Collect all saved plans
    plan_files = [f for f in os.listdir() if f.startswith("daily_plan_") and f.endswith(".txt")]
    if not plan_files:
        print("⚠️ No daily plan files found. Run daily_planner.py first.")
        return

    all_tasks = []
    for file in plan_files:
        all_tasks.extend(parse_plan_file(file))

    total_tasks = len(all_tasks)
    priorities = Counter([t["priority"] for t in all_tasks])
    times = Counter([t["time"] for t in all_tasks])

    busiest_day = max(plan_files, key=lambda f: os.path.getsize(f)).replace("daily_plan_", "").replace(".txt", "")
    most_common_time = times.most_common(1)[0][0] if times else "N/A"

    print(f"\n🧩 Total Tasks Logged: {total_tasks}")
    for p, c in priorities.items():
        symbol = "🔥" if p.lower() == "high" else "⚙️" if p.lower() == "medium" else "🌙"
        print(f"{symbol} {p}: {c}")

    print(f"\n📅 Busiest Day (by file size): {busiest_day}")
    print(f"🕘 Most Common Time Slot: {most_common_time}")

    # Optional insights
    if "9AM" in most_common_time:
        insight = "You've been most focused in the morning — great start!"
    else:
        insight = "Try scheduling more early sessions for better focus."

    print(f"\n💡 Insight: {insight}")

    # Save summary
    today = datetime.date.today().strftime("%Y-%m-%d")
    report_name = f"weekly_report_{today}.txt"
    with open(report_name, "w", encoding="utf-8") as f:
        f.write("=== Weekly Report Summary ===\n")
        f.write(f"Total Tasks: {total_tasks}\n")
        for p, c in priorities.items():
            f.write(f"{p}: {c}\n")
        f.write(f"Busiest Day: {busiest_day}\n")
        f.write(f"Most Common Time Slot: {most_common_time}\n")
        f.write(f"Insight: {insight}\n")

    print(f"\n✅ Report saved to {report_name}")


if __name__ == "__main__":
    generate_weekly_report()