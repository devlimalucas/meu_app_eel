import os


def list_files(path="."):
    """Lista arquivos e diretórios de uma pasta."""
    try:
        # Retorna apenas nomes de arquivos e pastas
        return os.listdir(path)
    except Exception as e:
        # Em caso de erro, retorna uma lista com a mensagem
        return [f"Erro: {str(e)}"]
