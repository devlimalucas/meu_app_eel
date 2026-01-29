import eel
from src.file_manager import list_files

eel.init('web')


@eel.expose
def list_files_exposed(path="."):
    return list_files(path)


eel.start('index.html', size=(800, 600), mode="default")
