import click #to create a cli
import json #to save and load tasks from a file
import os #to check if the file exists

TODO_File = "todo.json"

# functions to load tasks from json file
def load_tasks():
    if not os.path.exists(TODO_File):
        return []
    with open(TODO_File, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_File, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass
@click.command()
@click.argument("task")
def add(task):
    """Add a new task in the list"""
    tasks= load_tasks()
    tasks.append({"task" : task, "done" : False})
    save_tasks(tasks)
    click.echo(f"{task} added successfully")


@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status= "done" if task["done"] else "Pending"
        click.echo(f"{index}. {task["task"]} [{status}] ")


@click.command()   
@click.argument("task_number", type=int)     
def complete(task_number):
    """Mark a task completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} completed")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number): 
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {task_number} removed: {remove_task['task']}")  
    else:
        click.echo(f"Invalid task number: {task_number}")       


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)


if __name__ == "__main__":
    cli()

