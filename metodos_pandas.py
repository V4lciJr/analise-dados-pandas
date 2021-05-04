import pandas as pd

# lendo arquivo csv, que se encontra no diretorio dataset, dentro do diretorio raiz
df = pd.read_csv("datasets/Gapminder.csv", error_bad_lines=False, sep=";")

# Visualizando as 5 primeiras linhas
# print(df.head())

# renomeando as colunas
df = df.rename(columns={"country": "Pais", "continent": "continente", "year": "ano", "lifeExp": "Expectativa de Vida",
                        "pop": "Popul. Total", "gdpPercap": "PIB"})

# imprimindo o total de linhas e colunas da base de dados
# print(df.shape)

# imprimindo apenas as colunas do conjunto de dados
# print(df.columns)

# imprimindo o tipo de dados de cada coluna
# print(df.dtypes)

# imprimindo as ultimas linhas do conjunto de dados
# print(df.tail())

# estatisticas do conjunto de dados
# print(df.describe())

# filtrando o conjunto de dados
oceania = df.loc[df["continente"] == "Oceania"]
# print(oceania)

# Agrupando dados com o groupBy
print(df.groupby("continente")["Pais"].nunique())  # retorna quantos paises tem no conjunto de dados, para cada
# continente

print(df.groupby("ano")["Expectativa de Vida"].mean())  # retorna a expectativa media de vida de cada ano
print(f'{df["PIB"].mean(): .2f}')  # retorna a media da coluna PIB
print(f'{df["PIB"].sum(): .2f}')  # retorna a soma da coluna PIB
