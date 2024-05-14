import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('cadastros.csv', header=None, names=['Nome', 'Endereço', 'Telefone', 'Email', 'Login', 'Senha'])

# Exibir os primeiros registros
print(df.head())

df.to_excel('cadastros.xlsx', index=False)

input('a')