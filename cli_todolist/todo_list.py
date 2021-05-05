import click
import os
import sqlite3

# TODO: No pun intended,
# IMPORTANT: Create a db connection 
# 1. Prompt user for chore/task and store task so it persists.
#    Using sqlite as data store seems okay. I need to build the api for that

# 2. User should enter infinite task until last prompt is blank
# 3. Do not store blank prompt, skip
# 4. Display all tasks with the 'show' subcommand
# 5. Delete completed tasks from storage, indicating completion 
# 6. Edit a task entry CRUD Applications



# DB Connections

conn = sqlite3.connect("todo_list.db")
cursor = conn.cursor()
sqlite_query = """CREATE TABLE IF NOT EXISTS todo_list 
                  (date_added DATETIME DEFAULT CURRENT_TIMESTAMP, task TEXT NOT NULL, deadline TEXT)"""
cursor.execute(sqlite_query)
cursor.close()




@click.group()
def cli():
	"""A simple CLI Todo List, never worry about forgetting your tasks"""
	click.echo("Got tasks today? List 'em\n")

@cli.command()
def add():
	"""
	Add a new chore to your list in a repeated manner.
	Stop adding by making the next entry empty
	"""
	insert_query  = "INSERT INTO todo_list(task) VALUES(?)"
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

	print('Date | Task')
	for task_value in data:
		date, task, deadline = task_value
		print(task)
		


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


@cli.command()
def edit():
	pass


cli.add_command(add)
cli.add_command(show)
cli.add_command(delete)
cli.add_command(edit)

if __name__ == "__main__":
	cli()