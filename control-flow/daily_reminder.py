# daily_reminder.py

# Prompt for a Single Task with EXACT prompts
task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.", end="")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.", end="")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.", end="")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority.", end="")

# Add immediate attention message if time-bound
if time_bound == "yes":
    print(" This task requires immediate attention today!")
else:
    print()