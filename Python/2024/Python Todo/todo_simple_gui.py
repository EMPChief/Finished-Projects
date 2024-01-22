import json
import datetime
import PySimpleGUI as sg

sg.theme("DarkPurple5")
window_title = 'TODO List - [favicon.ico]' #did not work

class FileOperations:
    filename = "db/db.json"

    @staticmethod
    def initialize_tasks():
        try:
            with open(FileOperations.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def update_tasks_file(tasks):
        try:
            with open(FileOperations.filename, "w") as file:
                json.dump(tasks, file, indent=4)
        except Exception as e:
            sg.PopupError(f"Error saving data to file: {e}", title="File Error")

class TaskOperations:
    @staticmethod
    def add_task(tasks, window):
        task_description = window['-TASK-'].get()
        if task_description:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {
                "description": task_description,
                "status": "ongoing",
                "created_at": current_time
            }
            tasks.append(new_task)
            FileOperations.update_tasks_file(tasks)
            window['-TASK-'].update('')
            TaskOperations.display_tasks(tasks, window)

    @staticmethod
    def edit_task(tasks, window, task_list):
        task_index = window['-TASKS-'].get_indexes()
        if task_index:
            task_index = task_index[0]
            old_task_description = tasks[task_index]["description"]
            new_task_description = window['-TASK-'].get()
            tasks[task_index]["description"] = new_task_description
            sg.Popup(f"Task updated from '{old_task_description}' to '{new_task_description}'", title="Task Updated")
            FileOperations.update_tasks_file(tasks)
            window['-TASK-'].update('')
            TaskOperations.display_tasks(tasks, window)

    @staticmethod
    def remove_task(tasks, window, task_list):
        task_index = window['-TASKS-'].get_indexes()
        if task_index:
            task_index = task_index[0]
            removed_task = tasks.pop(task_index)
            sg.Popup(f"Task '{removed_task['description']}' removed", title="Task Removed")
            FileOperations.update_tasks_file(tasks)
            TaskOperations.display_tasks(tasks, window)

    @staticmethod
    def complete_task(tasks, window, task_list):
        task_index = window['-TASKS-'].get_indexes()
        if task_index:
            task_index = task_index[0]
            task_to_complete = tasks[task_index]
            if task_to_complete["status"] == "complete":
                sg.Popup(f"Task '{task_to_complete['description']}' is already marked as complete", title="Task Completed")
            else:
                task_to_complete["status"] = "complete"
                sg.Popup(f"Task '{task_to_complete['description']}' marked as complete", title="Task Completed")
                FileOperations.update_tasks_file(tasks)
                TaskOperations.display_tasks(tasks, window)

    @staticmethod
    def display_tasks(tasks, window):
        task_list = [f"{task['description']} | Status: {task['status']}" for task in tasks]
        window['-TASKS-'].update(values=task_list)

def main():
    tasks = FileOperations.initialize_tasks()
    
    layout = [
        [sg.Text("Enter a new task:")],
        [sg.InputText(key='-TASK-'), sg.Button('Add'), sg.Button('Edit')],
        [sg.Listbox(values=[], size=(40, 10), key='-TASKS-'), sg.Button('Show Tasks')],
        [sg.Button('Remove'), sg.Button('Complete'), sg.Button('Quit')]
    ]

    window = sg.Window(window_title, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        elif event == 'Add':
            TaskOperations.add_task(tasks, window)
        elif event == 'Edit':
            TaskOperations.edit_task(tasks, window, values['-TASKS-'])
        elif event == 'Remove':
            TaskOperations.remove_task(tasks, window, values['-TASKS-'])
        elif event == 'Complete':
            TaskOperations.complete_task(tasks, window, values['-TASKS-'])
        elif event == 'Show Tasks':
            TaskOperations.display_tasks(tasks, window)

    window.close()

if __name__ == "__main__":
    main()
