from setuptools import setup


setup(
	name = "simple",
	version = "0.0.01",
	install_requires = ["Click",],
	py_modules = ["todo_list"],
	entry_points = """
	[console_scripts]
	add=todo_list:prompt_task
	"""
)
