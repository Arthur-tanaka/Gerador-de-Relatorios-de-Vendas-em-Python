from reader import carregar_csv
from analyzer import analisar_dados
from pdf import gerar_pdf
from charts import gerar_grafico_vendas_por_mes
from input_csv import criar_csv_interativo

criar_csv_interativo()

def main():
    df = carregar_csv("data/vendas.csv")
    
    metricas = analisar_dados(df)

    print("Total faturado", metricas["total_faturado"])
    print("Media", metricas["media"])
    print("Maior venda", metricas["maior_venda"])
    print("Menor venda", metricas["menor_venda"])
    print("\nVendas por mês:")
    print(metricas["vendas_por_mes"])

    gerar_grafico_vendas_por_mes(metricas["vendas_por_mes"])
    gerar_pdf(metricas)

if __name__ == "__main__":
    main()

