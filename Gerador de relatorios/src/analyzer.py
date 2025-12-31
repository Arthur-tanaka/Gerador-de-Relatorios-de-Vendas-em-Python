import pandas as pd

def analisar_dados(df: pd.DataFrame):
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]

    total_faturado = df["valor_total"].sum()
    media = df["valor_total"].mean()
    maior_venda = df["valor_total"].max()
    menor_venda = df["valor_total"].min()


    df["data"] = pd.to_datetime(df["data"])
    vendas_por_mes = (
        df.groupby(df["data"].dt.to_period("M"))["valor_total"]
        .sum()
        .sort_index()
    )

    return {
        "total_faturado": total_faturado,
        "media": media,
        "maior_venda": maior_venda,
        "menor_venda": menor_venda,
        "vendas_por_mes": vendas_por_mes
    }