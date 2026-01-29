import pytest
from src.file_manager import list_files


def test_list_files_returns_files(tmp_path):
    """Valida que arquivos criados em um diretório são listados corretamente."""
    (tmp_path / "file1.txt").write_text("conteudo")
    (tmp_path / "file2.csv").write_text("conteudo")

    result = list_files(tmp_path)

    assert "file1.txt" in result
    assert "file2.csv" in result


def test_list_files_empty_dir(tmp_path):
    """Valida que diretório vazio retorna lista vazia."""
    result = list_files(tmp_path)
    assert result == []
