from utility import FileOperations, TaskOperations, UserInterface



def main():
    tasks = FileOperations.initialize_tasks()
    while True:
        UserInterface.print_menu()
        action = input().strip().lower()
        if action in "add":
            TaskOperations.add_task(tasks)
        elif action in "show":
            UserInterface.show_tasks(tasks)
        elif action in "edit":
            TaskOperations.edit_task(tasks)
        elif action in "remove":
            TaskOperations.remove_task(tasks)
        elif action in "complete":
            TaskOperations.complete_task(tasks)
        elif action in "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
