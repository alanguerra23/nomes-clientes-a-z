import pandas as pd


df_original = pd.read_excel('sua_planilha.xlsx', header=None)

dfs_separados = {}

for _, row in df_original.iterrows():
    nome_cliente = row[0]
    
    primeira_letra = nome_cliente[0].upper()
    
    if primeira_letra in dfs_separados:
        dfs_separados[primeira_letra] = dfs_separados[primeira_letra]._append(row)
    else:
        dfs_separados[primeira_letra] = pd.DataFrame([row])
        
for letra, df in dfs_separados.items():
    df.to_excel(f'{letra}_clientes.xlsx', index=False, header=False)
