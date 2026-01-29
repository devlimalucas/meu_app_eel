from src.file_manager import list_files


def test_list_files_returns_list():
    result = list_files(".")
    assert isinstance(result, list)


def test_list_files_invalid_path():
    result = list_files("caminho_inexistente_123")
    assert any("Erro" in item for item in result)
