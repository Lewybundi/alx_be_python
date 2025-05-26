#!/usr/bin/python3
"""
Daily Task Reminder
Provides customized reminders for a single task based on priority and time sensitivity
"""

def get_user_input():
    """Gets and validates user input"""
    task = input("Enter your task: ").strip()
    while True:
        priority = input("Priority (high/medium/low): ").lower().strip()
        if priority in ('high', 'medium', 'low'):
            break
        print("Invalid priority. Please enter high, medium, or low.")
    
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
        if time_bound in ('yes', 'no'):
            break
        print("Please answer with yes or no.")
    
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    """Generates customized reminder message"""
    print()  # Blank line for better formatting
    
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Focus on this soon.")
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task with a deadline. Schedule time for it today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to complete it this week.")
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task but has a time constraint. Complete when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

def main():
    print("Daily Task Reminder\n" + "="*20)
    task, priority, time_bound = get_user_input()
    generate_reminder(task, priority, time_bound)
    print("\nTask reminder set successfully!")

if __name__ == "__main__":
    main()