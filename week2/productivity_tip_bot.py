# productivity_tip_bot.py
import random

# Define categorized tips
TIPS = {
    "focus": [
        "Work in focused 25-minute Pomodoro sessions.",
        "Mute notifications during deep work blocks.",
        "Start your day with the most important task first.",
        "Batch similar tasks together to maintain flow."
    ],
    "motivation": [
        "Visualize your end goal every morning.",
        "Celebrate small wins to build momentum.",
        "Remember: consistency beats intensity.",
        "Don’t wait for inspiration — start, and it will follow."
    ],
    "organization": [
        "Review and plan your day each morning.",
        "Keep a digital and physical to-do list synced.",
        "Use folders and naming conventions for clean projects.",
        "Declutter your workspace weekly for mental clarity."
    ],
    "energy": [
        "Take a 5-minute walk every hour.",
        "Hydrate before you caffeinate.",
        "Sleep 7–8 hours — it's non-negotiable.",
        "Stretch to reset your body between tasks."
    ]
}

def get_random_tip(category=None):
    """Return a random tip. If category given, pull from that list."""
    if category and category in TIPS:
        return random.choice(TIPS[category])
    else:
        all_tips = [tip for cat in TIPS.values() for tip in cat]
        return random.choice(all_tips)

def main():
    print("💡 Productivity Tip Bot 💡")
    print("---------------------------")
    print("Categories: focus | motivation | organization | energy | random")
    category = input("Choose a category or press Enter for random: ").strip().lower()

    tip = get_random_tip(category if category in TIPS else None)
    print(f"\n✨ Tip: {tip}\n")

    # Ask user if they want another tip
    while input("Get another tip? (y/n): ").lower() == "y":
        tip = get_random_tip(category if category in TIPS else None)
        print(f"\n✨ Tip: {tip}\n")

if __name__ == "__main__":
    main()
