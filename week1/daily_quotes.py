# daily_quotes.py
import random

# List of productivity quotes
quotes = [
    "Focus on being productive instead of busy.",
    "Do the hard jobs first. The easy jobs will take care of themselves.",
    "Simplicity boils down to two steps: Identify the essential. Eliminate the rest.",
    "The key is not to prioritize what's on your schedule, but to schedule your priorities.",
    "Small daily improvements over time lead to stunning results."
]

# Select a random quote
quote_of_the_day = random.choice(quotes)

# Print the quote
print("📌 Daily Productivity Quote:")
print(quote_of_the_day)
