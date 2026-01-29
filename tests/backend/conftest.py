import pytest
import pandas as pd
import base64
import io
from faker import Faker

# Instância do Faker com seed para resultados reprodutíveis
fake = Faker()
Faker.seed(1234)

# -------------------------
# Fixtures de sucesso
# -------------------------


@pytest.fixture
def sample_df():
    """DataFrame simples para testes básicos."""
    return pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})


@pytest.fixture
def sample_csv_base64(sample_df):
    """CSV em base64 gerado a partir de sample_df."""
    content = sample_df.to_csv(index=False)
    return base64.b64encode(content.encode("utf-8")).decode("utf-8")


@pytest.fixture
def sample_xlsx_base64(sample_df):
    """Excel em base64 gerado a partir de sample_df."""
    buffer = io.BytesIO()
    sample_df.to_excel(buffer, index=False)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


@pytest.fixture
def random_df():
    """DataFrame aleatório usando Faker, útil para testes parametrizados."""
    data = {
        fake.word(): [fake.random_int(min=0, max=100) for _ in range(5)]
        for _ in range(3)
    }
    return pd.DataFrame(data)

# -------------------------
# Fixtures de erro
# -------------------------


@pytest.fixture
def invalid_csv_base64():
    """CSV corrompido em base64 (bytes inválidos)."""
    return base64.b64encode(b"\x00\xFF\xFE\xFDnot_a_csv").decode("utf-8")


@pytest.fixture
def invalid_xlsx_base64():
    """Excel inválido em base64 (conteúdo não é um arquivo válido)."""
    return base64.b64encode(b"conteudo_invalido").decode("utf-8")


@pytest.fixture
def invalid_base64_string():
    """String que não é base64 válida."""
    return "%%%INVALID%%%BASE64%%%"
