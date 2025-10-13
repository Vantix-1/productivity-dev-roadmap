import time

print("⏳ Simple Focus Timer")
seconds = int(input("Enter focus time in seconds: "))

for remaining in range(seconds, 0, -1):
    print(f"Time left: {remaining} seconds", end="\r")
    time.sleep(1)

print("\n✅ Time’s up! Stay consistent and keep pushing forward.")
