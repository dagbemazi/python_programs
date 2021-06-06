from setuptools import setup


setup(
        name="todo_list",
        version="0.1",
        install_requires=["Click", ],
        py_modules=["todo_list"],
        entry_points="""
	[console_scripts]
	add=todo_list:add
	show=todo_list:show
	delete=todo_list:delete
	edit=todo_list:edit
	"""
)
