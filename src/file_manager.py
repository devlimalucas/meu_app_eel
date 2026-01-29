import os


def list_files(path="."):
    """Lista arquivos e diretórios de uma pasta."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Erro: {str(e)}"]
