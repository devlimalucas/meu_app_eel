import pytest
from src.data_manager import analyze_file


def test_analyze_file_invalid_format_returns_error():
    """Valida que formatos não suportados retornam erro."""
    result = analyze_file("abc123", "dados.txt")
    assert result["Erro"] == "Formato não suportado"


@pytest.mark.parametrize("fixture_name, filename", [
    ("invalid_csv_base64", "dados.csv"),
    ("invalid_xlsx_base64", "dados.xlsx"),
    ("invalid_base64_string", "dados.csv"),
])
def test_analyze_file_invalid_content_returns_error(request, fixture_name, filename):
    """Valida que conteúdos inválidos retornam erro."""
    invalid_content = request.getfixturevalue(fixture_name)
    result = analyze_file(invalid_content, filename)
    assert "Erro" in result


def test_analyze_file_csv_read_error(monkeypatch, sample_csv_base64):
    """Simula falha no pandas.read_csv usando monkeypatch."""
    def fake_read_csv(*args, **kwargs):
        raise ValueError("falha simulada")

    monkeypatch.setattr("pandas.read_csv", fake_read_csv)

    result = analyze_file(sample_csv_base64, "dados.csv")
    assert "Erro" in result


def test_analyze_file_excel_read_error(monkeypatch, sample_xlsx_base64):
    """Simula falha no pandas.read_excel usando monkeypatch."""
    def fake_read_excel(*args, **kwargs):
        raise ValueError("falha simulada")

    monkeypatch.setattr("pandas.read_excel", fake_read_excel)

    result = analyze_file(sample_xlsx_base64, "dados.xlsx")
    assert "Erro" in result
