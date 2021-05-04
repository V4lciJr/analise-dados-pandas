import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

df = pd.read_excel("datasets/AdventureWorks.xlsx")

# print(df.head())

# print(df.dtypes)

""" Qual foi a receita total ? """
# print(f'Recita total: R$ {df["Valor Venda"].sum():.2f}')

""" Qual o custo total ? """
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

# Com o custo e a receita, podemos obter o lucro
df["Lucro"] = df["Valor Venda"] - df["Custo"]

# Lucro total
lucro_total = round(df["Lucro"].sum(), 2)
# print(lucro_total)

# Criando um coluna com o total de dias para enviar o produto
# df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

# extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# media de tempo de envio por marca
media_tempo = df.groupby("Marca")["Tempo_envio"].mean()
# print(media_tempo)

# Varificando valores ausentes
# print(df.isnull().sum())

""" Agrupando por lucro e por marca"""
lucro_marca = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()
# print(lucro_marca)

""" Qual o total de produtos vendidos ? """
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Grafico Total de produtos vendidos
#df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
# plt.show()

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro x Ano", color="red")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()
