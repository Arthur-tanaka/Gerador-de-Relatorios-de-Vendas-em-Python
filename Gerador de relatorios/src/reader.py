from pathlib import Path
import pandas as pd

caminho_arquivo = 'data/vendas.csv'
 
def carregar_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df
