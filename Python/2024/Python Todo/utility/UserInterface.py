from .TaskOperations import TaskOperations

class UserInterface:
    @staticmethod
    def show_tasks(tasks):
        if tasks:
            print("\nCurrent Tasks:")
            TaskOperations.display_tasks(tasks)
            print("\nEnd of Task List.\n")
        else:
            print("\nNo tasks available. Your list is all clear!\n")

        input("Press Enter to continue...")

    @staticmethod
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
