# Analise de dados com Python e pandas

>Notas das aulas da professora Fernanda Santos da Digital Innovation One.

<p>
Neste projeto exploraremos a biblioteca Pandas, da linguagem Python de código aberto para análise de dados. Ela dá a linguagem a capacidade de trabalhar com dados do tipo planilha, permitindo carregar, manipular e combinar dados rapidamente, entre outras funções.
</p>

Materiais utlizados:
- Ide PyCharm
- Anoconda Python

Começamos então com uma pequena definição do que é Data Science.
## Data Science
<p>
É uma ciência que estuda as informações, seu processo de captura, transformação, geração e posteriormente, análise de dados.
As linguagens mais utilizadas no momento são Python e R, com  um crescente uso também, das linguagens Julia e Scala
</p>
## Introdução ao Pandas
Primeiro temos que importat a biblioteca, com o comando:
**import pandas as pd***

onde este as pd, é um apelido que estamos dando a biblioteca, para não termos usar sempre o nome pandas, nas invocações de seus métodos. Se você estiver utilizando o google colab ou o ananconda python, esta biblioteca já vem integrada em sua implementação, caso você esteja usando o python puro, terá que instalar a biblioteca, caso esteja usando o pip, digite o comando **pip install pandas** no terminal, que a biblioteca será instalada.
A seguir para lermos um arquivo csv, usamos o metódo read_csv, instaciamos um dataframe, que receberá este arquivo lido.
**df = pd.read_csv("caminho_para_o_arquivo", error_bad_lines=False, sep=";")**. O primeiro parametro é o caminho para o arquivo, o parametro error_bad_lines = False, indica que as linhas contendo erros, serão ignoradas no momento da leitura e o separador que é o parametro sep, indica qual é o tipo de separador deste arquivo csv, que naturalmente é a vírgula, mas no caso deste exemplo, o arquivo foi separado com  **";"**.

