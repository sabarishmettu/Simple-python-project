import typer

app = typer.Typer()

tasks = []

@app.command()
def add(task: str):
    tasks.append(task)
    typer.echo(f"Added task: {task}")

@app.command()
def list():
    if not tasks:
        typer.echo("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):
            typer.echo(f"{i+1}. {task}")

@app.command()
def done(task_number: int):
    try:
        task = tasks.pop(task_number - 1)
        typer.echo(f"Marked task '{task}' as done.")
    except IndexError:
        typer.echo("Invalid task number.")

if __name__ == "__main__":
    app()



#python todo.py add "Buy groceries"
#python todo.py add "Finish project"
#python todo.py list
#python todo.py done 1
#python todo.py list

