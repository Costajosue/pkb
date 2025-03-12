# Para começar ler o Arquivo\Documentoção sobre o pandas: 
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html


# pandas é um pacote Python que fornece estruturas de dados rápidas, flexíveis e expressivas, projetadas para tornar 
# o trabalho com dados “relacionais” ou “rotulados” fácil e intuitivo. Ele tem como objetivo ser o bloco de construção
# fundamental de alto nível para fazer análises práticas de dados do mundo real em Python. Além disso, ele tem o objetivo 
# mais amplo de se tornar a ferramenta de análise/manipulação de dados de código aberto mais poderosa e flexível disponível 
# em qualquer linguagem . Ele já está bem encaminhado para atingir esse objetivo.


# Como importar o pandas:
import pandas as pd

# representação de tabela de dados pandas:
# Exemplo:

# Quero armazenar dados de passageiros do Titanic. Para vários passageiros, sei os dados de nome 
# (caracteres), idade (inteiros) e sexo (masculino/feminino).
DataFrame = pd.DataFrame(
    {
        "Nome":[
            "Mikael Costa Silva",
            "Daniel Carvalho Silva",
            "Camila Gimaraes Costa"
        ],
        "Idade":[19, 15, 26],
        "Sexo":["Masculino", "Masculino", "Feminino"],
    }
)
#print(DataFrame)

# Para armazenar dados manualmente em uma tabela, crie um DataFrame. Ao usar um dicionário Python de listas, as chaves do dicionário 
# serão usadas como cabeçalhos de coluna e os valores em cada lista como colunas do DataFrame.

# Cada Coluna de um Dataframe e uma "Series"

# Exemplo:

# Estou interessado apenas em trabalhar com os dados da colunaAge:

        # print(DataFrame["Idade"])

# Podemos também pode criar um a series zero:

        # Nacionalidades = pd.Series(["Brasil","Italia","Africa"], name= "Nacionalidade")
        # print(DataFrame)

#Faça algo com um DataFrame ou Series

# Exemplo:

# Quero saber a idade máxima dos passageiros:

        # print(DataFrame["Idade"].max()) # A função "max() é utilizada para filtrar nesse exemplo a maior idade"

# Exemplo:

# Estou interessado em algumas estatísticas básicas dos dados numéricos da minha tabela de dados:        
        #print(DataFrame.describe())

# Transformar em ukma planilia em exel de forma simples:
# print(DataFrame.to_excel("teste03.xlsx", sheet_name="passagem", index=False))
# print(DataFrame.head())
#finalizando