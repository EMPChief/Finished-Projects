import json
from pathlib import Path
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

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

