import matplotlib.pyplot as plt


def gerar_grafico_vendas_por_mes(vendas_por_mes):
    meses = vendas_por_mes.index.astype(str)
    valores = vendas_por_mes.values

    plt.figure(figsize=(8, 4))
    plt.plot(meses, valores, marker="o")
    plt.title("Vendas por mês")
    plt.xlabel("Mês")
    plt.ylabel("Valor vendido (R$)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("vendas_por_mes.png")
    plt.close()
