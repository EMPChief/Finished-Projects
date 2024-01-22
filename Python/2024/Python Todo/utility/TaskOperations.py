from .FileOperations import FileOperations
import datetime

class TaskOperations:
    @staticmethod
    def add_task(tasks):
        task_description = input("Enter a new task: ")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = {
            "description": task_description, 
            "status": "ongoing",
            "created_at": current_time
        }
        tasks.append(new_task)
        FileOperations.update_tasks_file(tasks)

    @staticmethod
    def edit_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to edit: "))
            old_task_description = tasks[task_index]["description"]
            new_task_description = input("Enter the new task description: ")
            tasks[task_index]["description"] = new_task_description
            print(f"Task updated from '{old_task_description}' to '{new_task_description}'")
            FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def remove_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to remove: "))
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['description']}' removed.")
            FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def complete_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to mark as complete: "))
            task_to_complete = tasks[task_index]
            if task_to_complete["status"] == "complete":
                print(f"Task '{task_to_complete['description']}' is already marked as complete.")
            else:
                task_to_complete["status"] = "complete"
                print(f"Task '{task_to_complete['description']}' marked as complete.")
                FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def display_tasks(tasks):
        for index, task in enumerate(tasks):
            print(f"{index}: {task['description']} | Status: {task['status']}")
