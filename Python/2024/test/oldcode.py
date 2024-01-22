import os
import time
tasks = []
filename = "tasks.txt"

if not os.path.exists(filename):
    open(filename, "w").close()


with open(filename, "r") as file:
    tasks = file.read().splitlines()

while True:
    action = input("Actions:\nAdd\nShow\nEdit\nRemove\nComplete\nQuit\nChoose and action: ").strip().lower()

    if action == "add":
        task = input("Enter a new task: ")
        tasks.append(task)
        with open(filename, "a") as file:
            file.write(f"{task}\n")

    elif action == "show":
        for item in tasks:
            print(f"Task: {item}")
        time.sleep(2)

    elif action == "edit":
        print("Current tasks:")
        for index, item in enumerate(tasks):
            print(f"{index}: {item}")
        try:
            task_index = int(input("Enter the number of the task to edit: "))
            old_task = tasks[task_index]
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            print(f"Task updated from '{old_task}' to '{new_task}'")
            with open(filename, "w") as file:
                file.write("\n".join(tasks))
        except (ValueError, IndexError):
            print("Invalid task number")

    elif action == "remove":
        try:
            for index, item in enumerate(tasks):
                print(f"{index}: {item}")
            task_index = int(input("Enter the number of the task to remove: "))
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
            with open(filename, "w") as file:
                file.write("\n".join(tasks))
        except (ValueError, IndexError):
            print("Invalid task number")

    elif action == "complete":
        print("Current tasks:")
        for index, item in enumerate(tasks):
            print(f"{index}: {item}")
        try:
            task_index = int(input("Enter the number of the task to mark as complete: "))
            task_to_complete = tasks[task_index]
            if "(complete)" in task_to_complete:
                print(f"Task '{task_to_complete}' is already marked as complete.")
            else:
                tasks[task_index] = task_to_complete + " (complete)"
                print(f"Task '{task_to_complete}' marked as complete.")
                with open(filename, "w") as file:
                    file.write("\n".join(tasks))
        except (ValueError, IndexError):
            print("Invalid task number")

    elif action in ['quit']:
        print("Goodbye!")
        break

    else:
        print("Invalid action")
