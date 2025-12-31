import pandas as pd
from datetime import datetime

def criar_csv_interativo(caminho_saida="data/vendas.csv"):
    vendas=[]

    print("=== Cadastro de vendas ===")

    while True:
        data = input("Data da venda (YYYY-MM-DD): ")

        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            print("Data inválida, use o formato (YYYY-MM-DD)")
            continue

        produto = input("Produto: ")
 
        try:
            quantidade = int(input("Quantidade: "))
            preco_unitario = float(input("Preço unitário: "))
        except ValueError:
            print("Quantidade e preço precisam ser números.")
            continue
        
        vendas.append({
            "data": data,
            "produto": produto,
            "quantidade": quantidade,
            "preco_unitario": preco_unitario
        })


        continuar = input("Adicionar outra venda? (s/n): ").lower()
        if continuar != "s":
            break

    df = pd.DataFrame(vendas)
    df.to_csv(caminho_saida, index=False)

    print(f"\nCSV criado com sucesso em: {caminho_saida}")