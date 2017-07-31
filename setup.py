import cx_Freeze

executables = [cx_Freeze.Executable("snakeGame.py")]

cx_Freeze.setup(
    name="Snake",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple.jpg","gameicon.png","snakehead.png"]}},
    description = "Snake Game",
    executables = executables
    )
