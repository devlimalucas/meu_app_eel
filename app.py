import eel
from src import list_files, analyze_file

eel.init('web')


@eel.expose
def list_files_exposed(path="."):
    return list_files(path)


@eel.expose
def save_and_analyze(base64_content, filename):
    return analyze_file(base64_content, filename)


eel.start('index.html', size=(800, 600), port=8000, mode="default")
