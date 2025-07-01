import pandas as pd

# Dados dos Pedidos
dados_pedidos = {
    'ID_Pedido': [101, 102, 103, 104, 105, 106],
    'ID_Cliente': [1, 2, 1, 3, 2, 1],
    'Valor': [250.50, 89.90, 149.99, 549.00, 320.00, 780.80]
}
pedidos_df = pd.DataFrame(dados_pedidos)

# Dados dos Clientes
dados_clientes = {
    'ID_Cliente': [1, 2, 3, 4],
    'Nome': ['João Silva', 'Maria Santos', 'Carlos Souza', 'Ana Ferreira'],
    'Estado': ['SP', 'RJ', 'SP', 'MG']
}
clientes_df = pd.DataFrame(dados_clientes)

df_completo = pd.merge(pedidos_df, clientes_df, on="ID_Cliente")

df_completo = df_completo.set_index("ID_Pedido")

faturamento_estados = df_completo.groupby("Estado")["Valor"].sum()

estado_maior_faturamento = faturamento_estados.idxmax()

clientes_compras = df_completo.groupby("ID_Pedido")[["Valor", "Nome"]].sum()

cliente_maior_compra = clientes_compras.sort_values(by="Valor", ascending=False).iloc[0]


print(faturamento_estados)
print(f"O estado com maior faturamento total foi {estado_maior_faturamento}")
print(f"O cliente que fez a maior compra foi {cliente_maior_compra['Nome']}, com o Valor de = {cliente_maior_compra['Valor']}")