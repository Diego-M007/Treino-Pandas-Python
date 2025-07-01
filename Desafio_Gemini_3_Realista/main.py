import pandas as pd
import numpy as np # A biblioteca numpy é usada aqui para representar valores ausentes (NaN)

dados_rh = {
    'ID_Funcionario': [101, 102, 103, 104, 105, 106],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva', 'Felipe'],
    'Cargo': ['Analista Jr', 'analista pleno', 'Gerente', 'ANALISTA JR', 'Estagiário', 'Analista Pleno'],
    'Departamento': ['Financeiro', 'T.I.', 'Financeiro', np.nan, 'T.I.', 'Marketing'],
    'Salario': ['R$ 4.500,50', 'R$ 7.800,00', 'R$ 12.000,00', 'R$ 4.650,20', 'R$ 1.500,00', 'R$ 7.950,90']
}

rh_df = pd.DataFrame(dados_rh)

# Tratamento de valor ausente em "Departamento"
rh_df['Departamento'] = rh_df["Departamento"].fillna("Não Alocado")

# Limpando coluna "Salário"
rh_df["Salario"] = rh_df["Salario"].str.replace("R$", "").str.replace(".", "").str.replace(",", ".")
rh_df['Salario'] = rh_df["Salario"].astype(float)

# Padronizando "Cargo" para letras minusculas
rh_df["Cargo"] = rh_df['Cargo'].str.lower()

# Criando uma nova coluna usando apply()

def Categoria_Cargo(salario):
    if salario < 2000:
        return "Estágiario"
    elif salario >= 2000 and salario < 5000:
        return "Júnior"
    elif salario >= 5000 and salario < 9000:
        return "Pleno"
    elif salario >= 9000:
        return "Sênior"
    else:
        return "Erro com dados"

rh_df["Nível"] = rh_df['Salario'].apply(Categoria_Cargo)



print(rh_df)