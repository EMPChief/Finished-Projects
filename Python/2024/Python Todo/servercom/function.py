import streamlit as st
import json

def showtask():
    try:
        with open("db/db.json", "r") as file:
            data = json.load(file)

        if data:
            st.write("### Task List:")
            for item in data:
                st.write(f"- **Task: {item['description']} | Status: {item['status']}**")
        else:
            st.write("### No tasks available. Your list is all clear!")
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
    except json.JSONDecodeError:
        st.error("Error in reading the JSON file.")

def edit_task(task_index, new_description):
    try:
        with open("db/db.json", "r") as file:
            task_data = json.load(file)

        if task_data:
            if task_index >= 0 and task_index < len(task_data):
                task_data[task_index]['description'] = new_description
                with open("db/db.json", "w") as file:
                    json.dump(task_data, file, indent=4)
            else:
                st.error("Invalid task index.")
        else:
            st.write("### No tasks available. Your list is all clear!")
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
    except json.JSONDecodeError:
        st.error("Error in reading the JSON file.")
