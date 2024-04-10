import pandas as pd

# Carregando a planilha original
df_original = pd.read_excel('sua_planilha.xlsx', header=None)

# Criando um dicionário vazio para armazenar os DataFrames de cada letra
dfs_separados = {}

# Iterando sobre cada linha da planilha original
for _, row in df_original.iterrows():
    # Obtendo o nome do cliente
    nome_cliente = row[0]
    
    # Obtendo a primeira letra do nome do cliente
    primeira_letra = nome_cliente[0].upper()
    
    # Verificando se a letra já existe no dicionário
    if primeira_letra in dfs_separados:
        dfs_separados[primeira_letra] = dfs_separados[primeira_letra]._append(row)
    else:
        dfs_separados[primeira_letra] = pd.DataFrame([row])

# Salvando os DataFrames separados em arquivos separados
for letra, df in dfs_separados.items():
    df.to_excel(f'{letra}_clientes.xlsx', index=False, header=False)
