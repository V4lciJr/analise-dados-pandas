import pandas as pd
import matplotlib.pyplot as plt

# leitura dos arquivos
df1 = pd.read_excel("datasets/Aracaju.xlsx")
df2 = pd.read_excel("datasets/Fortaleza.xlsx")
df3 = pd.read_excel("datasets/Natal.xlsx")
df4 = pd.read_excel("datasets/Recife.xlsx")
df5 = pd.read_excel("datasets/Salvador.xlsx")

# juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# exibindo as 5 primeiras linhas
# print(df.head())

# Pegando uma amostra do conjunto de dados
# print(df.sample(5))

# Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")
# print(df.dtypes)

# Somando linhas com valores faltantes
# print(df.isnull().sum())

# substituindo os valores nulos pela media
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valore nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)


""" Criando novas colunas """

df["Receita"] = df["Vendas"].mul(df["Qtde"])  # criando a coluna receita, com a multiplicacao do valor da coluna vendas
                                              # pelo valor da coluna qtde
# print(df.head())

df["Receitas / Vendas"] = df["Receita"] / df["Vendas"]

# retornando a maior receita
# print(df["Receita"].max())

# retornando a menor receita
# print(df["Receita"].min())

# retorna o top 3 com base na coluna receita
# as 3 maiores receitas
# print(df.nlargest(3, "Receita"))

# retorna o top 3 com base na coluna receita
# as 3 piores receitas
# print(df.nsmallest(3, "Receita"))

# Agrupando por cidade de retornando a soma da receita ordenada pela maior receita
# print(df.groupby("Cidade")["Receita"].sum().sort_values(ascending=False))

# Ordenando conjunto de dados
# print(df.sort_values("Receita", ascending=False).head(10))


"""  Trabalhando com Datas """

# Transformando a coluna de datas no tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Transformando a coluna de datas em datetime
df["Data"] = pd.to_datetime(df["Data"])

# Agrupando por ano
# print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna contendo o ano
df["Ano_Venda"] = df["Data"].dt.year
# print(df.sample(5))

# Extraindo o mes e o dia
df["Mes_Venda"], df["Dia_Venda"] = (df["Data"].dt.month, df["Data"].dt.day)
# print(df.sample(5))

# Retornando a data mais antiga
df["Data"].min()

# Calculando a diferenca de datas
df["Diferenca_data"] = df["Data"] - df["Data"].min()

# Criando a coluna de semestre
df["trimestre_venda"] = df["Data"].dt.quarter
#print(df.sample(5))

# filtrando as vendas de 2019 do mes de março
vendas_marco_19 = df.loc[(df["Ano_Venda"] == 2019) & (df["Mes_Venda"] == 3)]
#print(vendas_marco_19)


""" Visualizando Dados """

# Criando um grafico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()
plt.show()