import click
import sqlite3


@click.group()
def cli():
	"""A simple CLI Todo List, never worry about forgetting your tasks"""

	# Create DB
	conn = sqlite3.connect("todo_list.db")
	cursor = conn.cursor()
	sqlite_query = """CREATE TABLE IF NOT EXISTS todo_list 
					(date_added DATETIME DEFAULT CURRENT_TIMESTAMP, task TEXT NOT NULL, deadline TEXT)"""
	cursor.execute(sqlite_query)
	cursor.close()



@cli.command()
def add():
	"""
	Add a new chore to your list in a repeated manner.
	Stop adding by making the next entry empty
	"""
	insert_query  = "INSERT INTO todo_list(task) VALUES(?)"
	
	click.echo("Add tasks to your list.\n")

	while True:
		connect = sqlite3.connect("todo_list.db", timeout=100)
		cursor = connect.cursor()
		tasks = input("Task: ")
		if tasks != "":
			cursor.execute(insert_query, [tasks])
			connect.commit()
		else:
			break
	click.echo("\nTask(s) added to list successfully!")


@cli.command()
def show():
	"""
	Display all task in list.
	"""
	show_query = "SELECT * FROM todo_list"
	connect = sqlite3.connect("todo_list.db", timeout=100)
	cursor = connect.cursor()
	cursor.execute(show_query)
	data = cursor.fetchall()

	print(f"Date|Task|Deadline")
	for task_value in data:
		date, task, deadline = task_value
		if deadline == None:
			deadline = ""
		new_date = date.split()[0]
		click.echo(f"{new_date}|{task}|{deadline}")
		


@cli.command()
@click.argument("task", type=str)
def delete(task):
	"""
	Delete a task in the list.
	"""
	del_query = "DELETE FROM todo_list WHERE task=?"
	confirm_deletion = input("Are sure of deletion?\ny or n: ").lower()
	if confirm_deletion.startswith("y"):
		connect = sqlite3.connect("todo_list.db", timeout=100)
		cursor = connect.cursor()
		cursor.execute(del_query, [task])
		connect.commit()
		click.echo("\nTask deleted.")
	

@cli.command()
@click.argument("task", type=str)
@click.argument("edit_task")
def edit(task, edit_task):
	"""
	Edit a task in the list.
	"""
	edit_query = "UPDATE todo_list SET task = ? WHERE task = ?"
	conn = sqlite3.connect("todo_list.db")
	cursor = conn.cursor()
	cursor.execute(edit_query, (edit_task, task))
	conn.commit()
	click.echo("Successfully updated!")


# Add various commands to group
cli.add_command(add)
cli.add_command(show)
cli.add_command(delete)
cli.add_command(edit)

if __name__ == "__main__":
	cli()