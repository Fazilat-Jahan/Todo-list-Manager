# Todo List Manager

A simple command-line to-do list manager built using Python and Click, managed using UV package manager. This tool allows you to add, list, complete, and remove tasks, storing them in a JSON file.

## Getting Started

## Requirements:
Ensure you have Python installed.

### 1️⃣ Install UV
First, install UV (if not already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:

```sh
uv --version
```

### 2️⃣ Create and Initialize the Project
```sh
uv init todo-manager
cd todo-manager
```

### 3️⃣ Install Click (Dependency)
```sh
uv add click
```

### 4️⃣ Activate UV Virtual Environment
For Windows:
```sh
.venv\Scripts\activate
```
For Linux/macOS:
```sh
source .venv/bin/activate
```

## Features
- Add tasks to your to-do list
- List all tasks with their status (Pending/Done)
- Mark tasks as completed
- Remove tasks from the list
- Persistent storage using a JSON file

## Usage
Run the script using the following commands:

### Add a Task
```sh
uv python todo.py add "Task description"
```
Example:
```sh
uv python todo.py add "Complete Python project"
```

### List All Tasks
```sh
uv python todo.py list
```
This will display all tasks with their completion status.

### Mark a Task as Completed
```sh
uv python todo.py complete <task_number>
```
Example:
```sh
uv python todo.py complete 1
```
This marks task number 1 as completed.

### Remove a Task
```sh
uv python todo.py remove <task_number>
```
Example:
```sh
uv python todo.py remove 2
```
This removes task number 2 from the list.

## File Storage
The tasks are stored in a JSON file named `todo.json` in the same directory as the script. This ensures persistence across sessions.

## Notes
- If `todo.json` does not exist, it will be created automatically.
- Task numbers start from 1 when listing, completing, or removing tasks.

## License
This project is open-source and free to use.

## Reach Me on LinkedIn
If you have any questions or suggestions, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/fazilat-jahan-web-developer).


Happy task managing Folks! 

