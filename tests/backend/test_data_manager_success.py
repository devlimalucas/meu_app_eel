import pytest
import base64
from src.data_manager import analyze_file, generate_stats


def test_generate_stats_returns_expected_values(sample_df):
    """Valida estatísticas geradas a partir de um DataFrame simples."""
    stats = generate_stats(sample_df)

    assert stats["linhas"] == 3
    assert stats["colunas"] == 2
    assert set(stats["colunas_nomes"]) == {"A", "B"}
    assert stats["media_por_coluna"]["A"] == 2
    assert stats["media_por_coluna"]["B"] == 5


@pytest.mark.parametrize("fixture_name, filename", [
    ("sample_csv_base64", "dados.csv"),
    ("sample_xlsx_base64", "dados.xlsx"),
])
def test_analyze_file_valid_formats(request, fixture_name, filename):
    """Valida que CSV e Excel válidos são processados corretamente."""
    base64_content = request.getfixturevalue(fixture_name)
    stats = analyze_file(base64_content, filename)

    assert stats["linhas"] == 3
    assert stats["colunas"] == 2
    assert set(stats["colunas_nomes"]) == {"A", "B"}


def test_analyze_file_csv_with_strings_success():
    """CSV válido contendo strings deve ser aceito normalmente."""
    content = "coluna1,coluna2\n1,2\nx,y"
    base64_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    result = analyze_file(base64_content, "dados.csv")

    assert result["linhas"] == 2
    assert set(result["colunas_nomes"]) == {"coluna1", "coluna2"}
