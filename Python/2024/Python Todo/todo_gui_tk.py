import tkinter as tk
from tkinter import simpledialog, messagebox, PhotoImage
import datetime
import os
import json
from pathlib import Path

class FileOperations:
    db_folder = Path("db")
    filename = db_folder / "db.json"

    @staticmethod
    def initialize_tasks():
        FileOperations.db_folder.mkdir(parents=True, exist_ok=True)

        if not FileOperations.filename.exists():
            with FileOperations.filename.open("w") as file:
                json.dump([], file, indent=4)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        root.title("Todo List")
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bmklogo1.png")
        self.logo = PhotoImage(file=logo_path)
        root.iconphoto(False, self.logo)

        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")

        bg_color = "#333333"
        fg_color = "#FFFFFF"
        text_bg_color = "#1E1E1E"

        root.configure(bg=bg_color)

        self.date_time_label = tk.Label(root, text="", bg=bg_color, fg=fg_color)
        self.date_time_label.pack()

        self.input_frame = tk.Frame(root, bg=bg_color)
        self.input_frame.pack()

        self.input_entry = tk.Entry(self.input_frame, width=40, bg=text_bg_color, fg=fg_color)
        self.input_entry.pack(side=tk.LEFT)

        add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, bg=bg_color, fg=fg_color)
        add_button.pack(side=tk.LEFT)

        self.text_area = tk.Text(root, height=20, width=60, bg=text_bg_color, fg=fg_color)
        self.text_area.pack()

        buttons_frame = tk.Frame(root, bg=bg_color)
        buttons_frame.pack()

        show_button = tk.Button(buttons_frame, text="Show Tasks", command=self.show_tasks, bg=bg_color, fg=fg_color)
        show_button.pack(side=tk.LEFT)

        edit_button = tk.Button(buttons_frame, text="Edit Task", command=self.edit_task, bg=bg_color, fg=fg_color)
        edit_button.pack(side=tk.LEFT)

        remove_button = tk.Button(buttons_frame, text="Remove Task", command=self.remove_task, bg=bg_color, fg=fg_color)
        remove_button.pack(side=tk.LEFT)

        complete_button = tk.Button(buttons_frame, text="Complete Task", command=self.complete_task, bg=bg_color, fg=fg_color)
        complete_button.pack(side=tk.LEFT)

        self.tasks = FileOperations.initialize_tasks()
        self.show_tasks()
        self.update_date_time()
        self.selected_task_index = None

    def update_date_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_label.config(text=current_time)
        self.date_time_label.after(1000, self.update_date_time)

    def add_task(self):
        task_description = self.input_entry.get()
        if task_description:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {
                "description": task_description,
                "status": "ongoing",
                "created_at": current_time
            }
            self.tasks.append(new_task)
            FileOperations.update_tasks_file(self.tasks)
            self.input_entry.delete(0, tk.END)
            self.show_tasks()

    def show_tasks(self):
        self.text_area.delete('1.0', tk.END)
        for index, task in enumerate(self.tasks):
            self.text_area.insert(tk.END, f"{task['description']} | Status: {task['status']}\n")
            self.text_area.tag_add(f"task_{index}", f"{index + 1}.0", f"{index + 1}.end")
            self.text_area.tag_bind(f"task_{index}", "<Button-1>", lambda event, index=index: self.select_task(index))
            self.text_area.tag_bind(f"task_{index}", "<Double-Button-1>", lambda event, index=index: self.toggle_complete(index))

    def select_task(self, index):
        if self.selected_task_index is not None:
            self.text_area.tag_configure(f"task_{self.selected_task_index}", background='')
        self.selected_task_index = index
        self.text_area.tag_configure(f"task_{index}", background='#0078d4')

    def toggle_complete(self, index):
        task = self.tasks[index]
        if task["status"] == "ongoing":
            task["status"] = "complete"
        else:
            task["status"] = "ongoing"
        FileOperations.update_tasks_file(self.tasks)
        self.show_tasks()

    def edit_task(self):
        if self.selected_task_index is not None:
            task_description = simpledialog.askstring("Edit Task", "Enter the new task description:", parent=self.root)
            if task_description:
                old_task_description = self.tasks[self.selected_task_index]["description"]
                self.tasks[self.selected_task_index]["description"] = task_description
                FileOperations.update_tasks_file(self.tasks)
                messagebox.showinfo("Task Updated", f"Task updated from '{old_task_description}' to '{task_description}'")
                self.show_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please click on a task to select it for editing.")

    def remove_task(self):
        if self.selected_task_index is not None:
            removed_task = self.tasks.pop(self.selected_task_index)
            FileOperations.update_tasks_file(self.tasks)
            messagebox.showinfo("Task Removed", f"Task '{removed_task['description']}' removed.")
            self.selected_task_index = None
            self.show_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please click on a task to select it for removal.")

    def complete_task(self):
        if self.selected_task_index is not None:
            task_to_complete = self.tasks[self.selected_task_index]
            if task_to_complete["status"] == "complete":
                messagebox.showinfo("Already Complete", f"Task '{task_to_complete['description']}' is already marked as complete.")
            else:
                task_to_complete["status"] = "complete"
                FileOperations.update_tasks_file(self.tasks)
                messagebox.showinfo("Task Completed", f"Task '{task_to_complete['description']}' marked as complete.")
                self.show_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please click on a task to select it for completion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
