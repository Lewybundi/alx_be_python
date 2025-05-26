#!/usr/bin/python3
"""
Daily Reminder System
Provides customized reminders for a single task based on priority and time sensitivity
"""

def main():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process and generate reminder
    print("\nReminder: ", end="")
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"'{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"'{task}' is a high priority task. Focus on this soon.")
        case "medium":
            if time_bound == "yes":
                print(f"'{task}' is a medium priority task with a deadline. Schedule time for it today.")
            else:
                print(f"'{task}' is a medium priority task. Plan to complete it this week.")
        case "low":
            if time_bound == "yes":
                print(f"'{task}' is a low priority task but has a time constraint. Complete when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered. Please use high/medium/low.")

    # Celebration message
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()