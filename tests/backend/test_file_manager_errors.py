import pytest
from src.file_manager import list_files


@pytest.mark.parametrize("invalid_path", [
    "caminho_inexistente",  # diretório que não existe
])
def test_list_files_invalid_path_returns_error(invalid_path):
    """Valida que caminhos inválidos retornam erro."""
    result = list_files(invalid_path)
    assert any("Erro" in item for item in result)


def test_list_files_oserror_monkeypatch(monkeypatch):
    """Simula OSError usando monkeypatch para garantir que exceções são tratadas."""
    def fake_listdir(path):
        raise OSError("falha simulada")

    # Substitui temporariamente os.listdir pela função fake
    monkeypatch.setattr("os.listdir", fake_listdir)

    result = list_files("qualquer_pasta")
    assert any("Erro" in item for item in result)
