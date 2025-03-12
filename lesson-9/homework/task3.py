import json
import csv

# File paths
json_file = r"D:\MAAB academy new\python\homework\lesson-9\homework\tasks.json"
csv_file = r"D:\MAAB academy new\python\homework\lesson-9\homework\tasks.csv"

# Function to load tasks from JSON file
def load_tasks():
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {json_file} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file}")
        return []

# Function to save tasks to JSON file
def save_tasks(tasks):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {json_file}")

# Function to display tasks
def display_tasks(tasks):
    print("\nTask List:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']} | Task: {task['task']} | Status: {status} | Priority: {task['priority']}")

# Function to calculate task statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = round(sum(task["priority"] for task in tasks) / total_tasks, 2) if total_tasks > 0 else 0

    print("\nTask Completion Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {avg_priority}")

# Function to convert tasks.json to tasks.csv
def convert_json_to_csv(tasks):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])

        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

    print(f"JSON data converted to CSV: {csv_file}")

# Main Program
tasks = load_tasks()

if tasks:
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_json_to_csv(tasks)

    # Example: Modify a task (Marking "Do laundry" as completed)
    tasks[0]["completed"] = True  
    save_tasks(tasks)  # Save changes
