import pandas as pd
import io
import base64


def generate_stats(df):
    return {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "colunas_nomes": list(df.columns),
        "media_por_coluna": df.mean(numeric_only=True).to_dict()
    }


def analyze_file(base64_content: str, filename: str):
    """Recebe conteúdo em base64 e o nome do arquivo, decide o tipo e gera estatísticas."""
    try:
        if filename.endswith(".csv"):
            content = base64.b64decode(base64_content).decode("utf-8")
            df = pd.read_csv(io.StringIO(content))
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            binary = base64.b64decode(base64_content)
            df = pd.read_excel(io.BytesIO(binary))
        else:
            return {"Erro": "Formato não suportado"}
        return generate_stats(df)
    except Exception as e:
        return {"Erro": str(e)}
