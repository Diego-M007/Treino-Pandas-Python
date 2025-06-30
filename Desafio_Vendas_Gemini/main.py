import pandas as pd
import openpyxl as pyxl

# DEFININDO O ARQUIVO COMO DATAFRAME
vendas_df = pd.read_excel("vendas.xlsx")

# LOCALIZAR INFORMAÇÕES BASEADO EM COMPARAÇÃO USANDO "=="
vendas_df["Valor Total"] = vendas_df["Preco_Unitario"] * vendas_df["Quantidade"]

faturamento_por_vendedor_df = vendas_df.groupby("Vendedor")[["Quantidade", "Valor Total"]].sum()

vendas_Ana_df = vendas_df.loc[vendas_df['Vendedor'] == "Ana"]
faturamento_total = vendas_df["Valor Total"].sum()
faturamento_ana = vendas_Ana_df["Valor Total"].sum()

produtos_mais_vendidos_df = vendas_df.groupby("Produto")[["Quantidade", "Valor Total"]].sum()

produto_mais_vendido = produtos_mais_vendidos_df["Quantidade"].idxmax()

# IMPRIMIR NA TELA
print(f"O faturamento total da empresa foi de:{faturamento_total}")
print(f"O faturamento da ana foi de: {faturamento_ana}")
print(produto_mais_vendido)

vendas_df.to_excel("Relatorio de Vendas atualizado.xlsx",index=False)


