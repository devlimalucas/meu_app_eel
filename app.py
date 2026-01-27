import eel
import os
from dotenv import load_dotenv

load_dotenv()
pasta = os.getenv("APP_FOLDER", ".")

eel.init('web')

@eel.expose
def listar_arquivos(pasta=pasta):
    return os.listdir(pasta)

@eel.expose
def get_env_folder():
    return pasta

eel.start('index.html', size=(800, 600), mode='default')
