# daily_reminder.py

# Prompt for a Single Task
task = input("Enter the task you need to do today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Provide a Customized Reminder
print(reminder)