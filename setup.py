from cx_Freeze import setup, Executable

setup(
    name = "TuxWorld",
    version = "2",
    descripcion = "Juego hecho por El gran DT & Newtonis",
    executables = [Executable("main.py")]
)