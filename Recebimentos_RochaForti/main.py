import pandas as pd

# --- Funções Especialistas ---
# Cada função tem uma única responsabilidade.

def definir_informacoes_iniciais():
    """Pede os pesos de cada embalagem e CRIA/RETORNA o DataFrame inicial."""
    lista_pesos_local = []
    quantidade_total_embalagens = int(input("Digite a quantidade TOTAL de embalagens: "))
    print("-" * 20)
    for i in range(quantidade_total_embalagens):
        peso_embalagem = float(input(f"Digite o peso da embalagem nº {i+1} (em gramas): "))
        lista_pesos_local.append(peso_embalagem)
    print("-" * 20)
    df = pd.DataFrame(lista_pesos_local, columns=["Peso Bruto (g)"])
    return df

# Funções que RETORNAM um valor único
def obter_produto():
    """Pede e RETORNA o nome do produto."""
    produto = input("Digite qual o produto está sendo recebido: ")
    return produto

def obter_peso_unitario():
    """Pede e RETORNA o peso unitário do produto."""
    peso_unitario = float(input("Digite o peso Unitário do produto (em gramas): "))
    return peso_unitario

def obter_peso_embalagem_vazia():
    """Pede e RETORNA o peso da embalagem vazia."""
    peso_embalagem_vazia = float(input("Digite o peso da embalagem vazia (em gramas): "))
    return peso_embalagem_vazia

def obter_unidades_por_embalagem():
    """Pede e RETORNA a quantidade de unidades por embalagem."""
    unidades_por_embalagem = int(input("Digite qual a quantidade de unidades em CADA embalagem: "))
    return unidades_por_embalagem

# Funções que CALCULAM e modificam o DataFrame
def calcular_colunas(df, produto, peso_unitario, peso_embalagem, unidades_embalagem):
    """Recebe o DF e os valores únicos, e adiciona todas as colunas de cálculo."""
    print("Adicionando colunas e calculando...")
    
    # Adicionando colunas com valores constantes
    df["Produto"] = produto
    df["Unidades por Embalagem"] = unidades_embalagem

    # Colunas calculadas
    df["Peso s/Embalagem (g)"] = df["Peso Bruto (g)"] - peso_embalagem
    df["Peso Ideal (g)"] = unidades_embalagem * peso_unitario
    df["Diferença de Peso (g)"] = df["Peso Ideal (g)"] - df["Peso s/Embalagem (g)"]
    df[f"Diferença em Unidades de {produto}"] = df["Diferença de Peso (g)"] / peso_unitario 


# --- Execução Principal do Código (O Maestro) ---

# 1. Criar a base do nosso relatório
pesos_df = definir_informacoes_iniciais()

# 2. Obter todas as informações que são únicas e ARMAZENAR em variáveis
nome_produto = obter_produto()
valor_peso_unitario = obter_peso_unitario()
valor_peso_embalagem_vazia = obter_peso_embalagem_vazia()
valor_unidades_por_embalagem = obter_unidades_por_embalagem()

# ... (todo o seu código anterior permanece exatamente o mesmo até aqui) ...

# 3. Chamar a função de cálculo, PASSANDO o DataFrame e todas as variáveis que ela precisa
calcular_colunas(
    pesos_df, 
    nome_produto, 
    valor_peso_unitario, 
    valor_peso_embalagem_vazia, 
    valor_unidades_por_embalagem
)

# --- Criação do Resumo e Geração do Relatório ---

# 4. Calcular as métricas de resumo
print("\nCalculando resumo do recebimento...")
peso_total_esperado = float(input("Digite qual o peso esperado na Nota Fiscal (em gramas): "))
media_pesos_brutos = pesos_df["Peso Bruto (g)"].mean()
peso_total_recebido = pesos_df["Peso Bruto (g)"].sum()
diferenca_peso_total = peso_total_recebido - peso_total_esperado # Inverti para ter um valor positivo se recebeu a mais
quantidade_total_embalagens = len(pesos_df) # Forma robusta de contar as embalagens

# 5. Criar um novo DataFrame para o resumo
# Usamos um dicionário para criar essa nova tabela de forma organizada.
dados_resumo = {
    "Métrica": [
        "Produto Recebido",
        "Quantidade de Embalagens",
        "Peso Total Esperado (g)",
        "Peso Total Recebido (g)",
        "Diferença vs. Nota Fiscal (g)",
        "Peso Médio por Embalagem (g)"
    ],
    "Valor": [
        nome_produto,
        quantidade_total_embalagens,
        peso_total_esperado,
        peso_total_recebido,
        diferenca_peso_total,
        media_pesos_brutos
    ]
}
resumo_df = pd.DataFrame(dados_resumo)


# 6. Imprimir o DataFrame principal e o resumo no terminal para conferência
print("\n--- Tabela Detalhada ---")
print(pesos_df)
print("\n--- Resumo do Recebimento ---")
print(resumo_df)


# 7. Salvar AMBOS os DataFrames em um único arquivo Excel com duas abas
nome_arquivo = f"Relatorio_{nome_produto}_{pd.Timestamp.now().strftime('%Y-%m-%d')}.xlsx"

# Usamos o ExcelWriter para gerenciar o arquivo
with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
    # Escreve o primeiro DataFrame na aba 'Detalhes'
    pesos_df.to_excel(writer, sheet_name='Detalhes do Recebimento', index=False)
    
    # Escreve o DataFrame de resumo na aba 'Resumo'
    resumo_df.to_excel(writer, sheet_name='Resumo', index=False)

print(f"\nRelatório com abas de Detalhes e Resumo salvo como '{nome_arquivo}'")

