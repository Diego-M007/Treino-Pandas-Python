import pandas as pd
# O import do openpyxl não é estritamente necessário para a leitura,
# pois o Pandas o usa "por baixo dos panos", mas não há problema em tê-lo.

# ==============================================================================
# 1. LEITURA E INSPEÇÃO BÁSICA
# ==============================================================================

# Carrega a planilha Excel para dentro de uma estrutura de dados do Pandas chamada DataFrame.
# Pense no DataFrame (df) como a sua planilha inteira dentro do Python.
vendas_df = pd.read_excel("vendas.xlsx")

# --- Formas de Visualizar e Inspecionar seu DataFrame ---

# Mostra as 5 primeiras linhas do DataFrame. Ótimo para uma verificação rápida.
print("--- 1.1. Visualizando as 5 primeiras linhas (head) ---")
print(vendas_df.head())

# Mostra as 5 últimas linhas.
print("\n--- 1.2. Visualizando as 5 últimas linhas (tail) ---")
print(vendas_df.tail())

# Fornece um resumo técnico: o tipo de dado de cada coluna, e quantos valores não-nulos existem.
# Essencial para verificar se o Pandas leu as colunas com os tipos corretos (número, texto, data).
print("\n--- 1.3. Informações técnicas do DataFrame (info) ---")
vendas_df.info()

# Mostra a quantidade de linhas e colunas (linhas, colunas).
print(f"\n--- 1.4. Dimensões do DataFrame (shape): {vendas_df.shape} ---")

# Mostra uma lista com todos os nomes das colunas.
print(f"\n--- 1.5. Nomes das colunas (columns): {vendas_df.columns.tolist()} ---")

# DEFINIR UMA COLUNA COMO INDEX

df_vendas = df_vendas.set_index("Data")


# ==============================================================================
# 2. SELEÇÃO E FILTRAGEM DE DADOS (SLICING & DICING)
# ==============================================================================

# --- Selecionando Colunas ---

# Para selecionar UMA única coluna (o resultado é uma 'Series' do Pandas).
print("\n--- 2.1. Selecionando uma única coluna ('Vendedor') ---")
print(vendas_df['Vendedor'])

# Para selecionar MÚLTIPLAS colunas (note os colchetes duplos [[]]). O resultado é um novo DataFrame.
print("\n--- 2.2. Selecionando múltiplas colunas ---")
print(vendas_df[['Vendedor', 'Produto', 'Quantidade']])


# --- Selecionando Linhas com base em Condições (Filtragem) ---

# Usa uma condição lógica para filtrar as linhas.
# "Me dê todas as linhas do vendas_df ONDE a coluna 'Vendedor' é igual a 'Ana'".
print("\n--- 2.3. Filtrando linhas com base em um valor exato (loc com '==') ---")
print(vendas_df.loc[vendas_df['Vendedor'] == "Ana"])

# A mesma lógica funciona para comparações numéricas.
# OBS: Esta linha precisa vir DEPOIS da criação da coluna "Valor Total".
# Por isso, vamos criá-la primeiro.
vendas_df["Valor Total"] = vendas_df["Preco_Unitario"] * vendas_df["Quantidade"]
print("\n--- 2.4. Filtrando linhas com base em um valor numérico (loc com '>') ---")
print(vendas_df.loc[vendas_df['Valor Total'] > 1000])

# Você pode combinar múltiplas condições usando & (E) e | (OU).
# Encontrar vendas da 'Ana' que foram maiores que R$ 300.
print("\n--- 2.5. Combinando múltiplas condições (& para 'E') ---")
print(vendas_df.loc[(vendas_df['Vendedor'] == "Ana") & (vendas_df['Valor Total'] > 300)])


# ==============================================================================
# 3. MANIPULAÇÃO DE COLUNAS E LINHAS
# ==============================================================================

# --- Colunas ---

# Criando uma nova coluna a partir de colunas existentes (você já fez isso perfeitamente).
# vendas_df["Valor Total"] = vendas_df["Preco_Unitario"] * vendas_df["Quantidade"]

# Criando uma nova coluna com um valor fixo para todas as linhas.
print("\n--- 3.1. Criando uma coluna com valor fixo ---")
vendas_df['Comissão (%)'] = 5
print(vendas_df.head())

# Usando .apply() para criar uma coluna com base em uma função personalizada.
# É uma das funções mais poderosas do Pandas!
print("\n--- 3.2. Criando uma coluna com .apply() ---")
def categorizar_venda(valor):
    if valor > 1000:
        return "Venda Grande"
    elif valor > 300:
        return "Venda Média"
    else:
        return "Venda Pequena"

vendas_df['Categoria Venda'] = vendas_df['Valor Total'].apply(categorizar_venda)
print(vendas_df[['Produto', 'Valor Total', 'Categoria Venda']].head())


# --- Linhas ---

# CORREÇÃO: O método .append() foi descontinuado. A forma moderna de juntar
# DataFrames é com pd.concat().
# Exemplo: Criando um novo DataFrame e juntando com o original.
nova_venda = pd.DataFrame([
    {'Data': '2025-06-29', 'Vendedor': 'Carlos', 'Produto': 'Monitor Ultrawide', 'Quantidade': 1, 'Preco_Unitario': 1800.00}
])
# ignore_index=True é importante para refazer o índice (0, 1, 2, ...).
vendas_df = pd.concat([vendas_df, nova_venda], ignore_index=True)
print("\n--- 3.3. Adicionando uma nova linha (concat) ---")
print(vendas_df.tail()) # Mostra as últimas linhas para vermos a nova venda


# --- Exclusão ---

# Excluir uma coluna (axis=1).
# vendas_df = vendas_df.drop("Comissão (%)", axis=1)

# Excluir uma linha pelo seu índice (axis=0).
# vendas_df = vendas_df.drop(0, axis=0) # Exclui a primeira linha


# ==============================================================================
# 4. TRATAMENTO DE DADOS AUSENTES (NaN)
# ==============================================================================
# Primeiro, vamos criar alguns dados ausentes para os exemplos.
vendas_df.loc[0, 'Valor Total'] = None

# Excluir todas as LINHAS que possuem PELO MENOS 1 valor vazio.
# df_sem_nan = vendas_df.dropna()

# Excluir todas as LINHAS onde TODOS os valores são vazios.
# df_sem_nan = vendas_df.dropna(how="all")

# Excluir COLUNAS que possuem algum valor vazio.
# df_sem_nan_colunas = vendas_df.dropna(axis=1)

# --- Preenchendo valores vazios (NaN) ---

# Preencher valores vazios na coluna "Valor Total" com o valor fixo 0.
# vendas_df["Valor Total"] = vendas_df["Valor Total"].fillna(0)

# Preencher com a MÉDIA da própria coluna (muito comum em análise de dados).
media_valor_total = vendas_df["Valor Total"].mean()
vendas_df["Valor Total"] = vendas_df["Valor Total"].fillna(media_valor_total)
print("\n--- 4.1. Preenchendo valores nulos com a média ---")
print(vendas_df.head())


# ==============================================================================
# 5. AGRUPAMENTO, AGREGAÇÃO E ESTATÍSTICAS
# ==============================================================================

# Contar quantas vezes cada valor único aparece em uma coluna.
print("\n--- 5.1. Contando vendas por vendedor (value_counts) ---")
print(vendas_df["Vendedor"].value_counts())

# Agrupar por uma coluna e aplicar uma função de agregação (soma, média, etc.).
# "Agrupe por Vendedor e, para cada vendedor, some as Quantidades e os Valores Totais".
print("\n--- 5.2. Agrupando e somando (groupby com sum) ---")
faturamento_por_vendedor = vendas_df.groupby("Vendedor")[["Quantidade", "Valor Total"]].sum()
print(faturamento_por_vendedor)

# Agrupando e calculando a média.
print("\n--- 5.3. Agrupando e calculando a média (groupby com mean) ---")
media_por_produto = vendas_df.groupby("Produto")[["Quantidade", "Valor Total"]].mean()
print(media_por_produto)


# ==============================================================================
# 6. ORDENAÇÃO E RANKING
# ==============================================================================

# Ordenar um DataFrame com base em uma coluna.
print("\n--- 6.1. Ordenando o faturamento por vendedor (sort_values) ---")
faturamento_ordenado = faturamento_por_vendedor.sort_values(by="Valor Total", ascending=False)
print(faturamento_ordenado)

# Descobrir o rótulo do índice (neste caso, o nome do produto) que contém o maior valor em uma coluna.
print("\n--- 6.2. Encontrando o item de maior valor (idxmax) ---")
produtos_agrupados = vendas_df.groupby("Produto")["Quantidade"].sum()
produto_mais_vendido = produtos_agrupados.idxmax()
print(f"O produto mais vendido em unidades foi: {produto_mais_vendido}")


# ==============================================================================
# 7. JUNTANDO DATAFRAMES (MERGE - similar ao PROCV/VLOOKUP do Excel)
# ==============================================================================

# Imagine que temos outro DataFrame com informações dos gerentes de cada vendedor.
gerentes_df = pd.DataFrame([
    {'Vendedor': 'Ana', 'Gerente': 'Lucas'},
    {'Vendedor': 'João', 'Gerente': 'Mariana'},
    {'Vendedor': 'Carlos', 'Gerente': 'Lucas'},
    {'Vendedor': 'Bia', 'Gerente': 'Mariana'}
])

# Usamos pd.merge() para juntar os dois DataFrames com base na coluna em comum ("Vendedor").
print("\n--- 7.1. Juntando DataFrames (merge) ---")
vendas_com_gerente_df = pd.merge(vendas_df, gerentes_df, on="Vendedor")
print(vendas_com_gerente_df.head())


# ==============================================================================
# 8. EXPORTANDO DADOS
# ==============================================================================

# Depois de todo o trabalho, você pode salvar o resultado em um novo arquivo.
# index=False evita que o Pandas salve o índice do DataFrame (0, 1, 2...) como uma coluna no Excel.
# vendas_com_gerente_df.to_excel("relatorio_final_vendas.xlsx", index=False)

print("\n--- Fim da Análise ---")