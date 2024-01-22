from flask import Flask, render_template, request, redirect, flash, url_for
import json
from pathlib import Path
import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.template_filter('enumerate')
def custom_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

class FileOperations:
    filename = Path("db/db.json")

    @staticmethod
    def initialize_tasks():
        if not FileOperations.filename.exists():
            FileOperations.filename.parent.mkdir(parents=True, exist_ok=True)
            with FileOperations.filename.open("w") as file:
                json.dump([], file, indent=4)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file, indent=4)

class TaskOperations:
    @staticmethod
    def add_task(description):
        try:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {
                "description": description,
                "status": "ongoing",
                "created_at": current_time
            }

            tasks = FileOperations.initialize_tasks()
            tasks.append(new_task)
            FileOperations.update_tasks_file(tasks)
            flash('Task added successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

    @staticmethod
    def edit_task(index, new_description):
        try:
            tasks = FileOperations.initialize_tasks()

            if index >= 0 and index < len(tasks):
                old_description = tasks[index]["description"]
                tasks[index]["description"] = new_description
                FileOperations.update_tasks_file(tasks)
                flash(f"Task updated from '{old_description}' to '{new_description}'", 'success')
            else:
                flash('Invalid task index.', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

    @staticmethod
    def remove_task(index):
        try:
            tasks = FileOperations.initialize_tasks()

            if index >= 0 and index < len(tasks):
                removed_task = tasks.pop(index)
                FileOperations.update_tasks_file(tasks)
                flash(f"Task '{removed_task['description']}' removed.", 'success')
            else:
                flash('Invalid task index.', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

    @staticmethod
    def complete_task(index):
        try:
            tasks = FileOperations.initialize_tasks()

            if index >= 0 and index < len(tasks):
                task_to_complete = tasks[index]
                if task_to_complete["status"] == "complete":
                    flash(f"Task '{task_to_complete['description']}' is already marked as complete.", 'info')
                else:
                    task_to_complete["status"] = "complete"
                    FileOperations.update_tasks_file(tasks)
                    flash(f"Task '{task_to_complete['description']}' marked as complete.", 'success')
            else:
                flash('Invalid task index.', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

@app.route('/')
def index():
    tasks = FileOperations.initialize_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    description = request.form.get('task_description')
    if description:
        TaskOperations.add_task(description)
    else:
        flash('Task description is empty.', 'danger')
    return redirect(url_for('index'))

@app.route('/edit_task/<int:index>', methods=['POST'])
def edit_task(index):
    new_description = request.form.get('new_description')
    TaskOperations.edit_task(index, new_description)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:index>', methods=['POST'])
def remove_task(index):
    TaskOperations.remove_task(index)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:index>', methods=['POST'])
def complete_task(index):
    TaskOperations.complete_task(index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
