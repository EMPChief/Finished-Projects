import os
import time

filename = "tasks.txt"

def initialize_tasks():
    if not os.path.exists(filename):
        open(filename, "w").close()

    with open(filename, "r") as file:
        return file.read().splitlines()

def update_tasks_file(tasks):
    with open(filename, "w") as file:
        file.write("\n".join(tasks))

def display_tasks(tasks):
    for index, item in enumerate(tasks):
        print(f"{index}: {item}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    update_tasks_file(tasks)

def show_tasks(tasks):
    if tasks:
        print("\nCurrent Tasks:")
        display_tasks(tasks)
        print("\nEnd of Task List.\n")
    else:
        print("\nNo tasks available. Your list is all clear!\n")

    input("Press Enter to continue...")


def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to edit: "))
        old_task = tasks[task_index]
        new_task = input("Enter the new task: ")
        tasks[task_index] = new_task
        print(f"Task updated from '{old_task}' to '{new_task}'")
        update_tasks_file(tasks)
    except (ValueError, IndexError):
        print("Invalid task number")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed.")
        update_tasks_file(tasks)
    except (ValueError, IndexError):
        print("Invalid task number")

def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to mark as complete: "))
        task_to_complete = tasks[task_index]
        if "(complete)" in task_to_complete:
            print(f"Task '{task_to_complete}' is already marked as complete.")
        else:
            tasks[task_index] = task_to_complete + " (complete)"
            print(f"Task '{task_to_complete}' marked as complete.")
            update_tasks_file(tasks)
    except (ValueError, IndexError):
        print("Invalid task number")

def print_menu():
    print("========== TODO LIST ==========")
    print("Actions:")
    print("1. Add")
    print("2. Show")
    print("3. Edit")
    print("4. Remove")
    print("5. Complete")
    print("6. Quit")
    print("===============================")
    print("Choose an action: ", end="")
    

def main():
    tasks = initialize_tasks()
    while True:
        print_menu()
        action = input().strip().lower()
        if action in "add":
            add_task(tasks)
        elif action in "show":
            show_tasks(tasks)
        elif action in"edit":
            edit_task(tasks)
        elif action in "remove":
            remove_task(tasks)
        elif action in "complete":
            complete_task(tasks)
        elif action in "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
