import pandas as pd

# Copie e cole este dicionário no seu script
dados_vendas = {
    'Data': [
        '2025-05-01', '2025-05-02', '2025-05-05', '2025-05-06', '2025-05-07', 
        '2025-05-08', '2025-05-09', '2025-05-12', '2025-05-13', '2025-05-14',
        '2025-05-15', '2025-05-16', '2025-05-19', '2025-05-20', '2025-05-21',
        '2025-05-22', '2025-05-23', '2025-05-26', '2025-05-27', '2025-05-28',
        '2025-05-29', '2025-05-30'
    ],
    'Valor_Venda': [
        1050.50, 980.20, 1500.00, 1340.75, 2100.10, 
        1980.00, 2300.50, 2550.00, 2680.30, 2750.00, 
        2890.90, 3100.00, 2950.00, 3200.60, 3150.80,
        3400.00, 3650.70, 3800.00, 4100.20, 4050.00,
        4300.50, 4500.00
    ]
}

vendas_df = pd.DataFrame(dados_vendas)

vendas_df["Data"] = pd.to_datetime(vendas_df['Data'], format="mixed",yearfirst=True)

vendas_df = vendas_df.set_index("Data")

# PEGANDO FATURAMENTOS DO MENOR E MAIOR DIA

dia_maior_venda = vendas_df['Valor_Venda'].idxmax()
valor_maior_venda = vendas_df['Valor_Venda'].max()
dia_menor_venda = vendas_df['Valor_Venda'].idxmin()
valor_menor_venda = vendas_df['Valor_Venda'].min()

# DIVIDINDO DATA POR SEMANA

vendas_semanal_df = vendas_df.resample("W").sum()

# TABELA ATUALIZADA
print(vendas_df)

# MOSTRANDO VALORES DE FATURAMENTO DO MENOR E MAIOR DIA
print("="*30)
print("Dia de Maior venda")
print(f"{dia_maior_venda.strftime('%d/%m/%Y ')}: {valor_maior_venda:.2f}")
print("="*30)
print("Dia de Menor venda")
print(f"{dia_menor_venda.strftime("%d/%m/%y")}: {valor_menor_venda:.2f}")  


# MONTRANDO O FATURAMENTO SEMANAL
print("="*30)
print("Faturamento Semanal")
print(vendas_semanal_df)
