import pandas as pd # importando o pandas.

# O pandas fornece a read_csv()função de ler dados armazenados como um arquivo csv em um pandas DataFrame. 
# O pandas suporta muitos formatos de arquivo ou fontes de dados diferentes prontos para uso (csv, excel, sql, json, parquet, …), 
# cada um deles com o prefixo read_*.

# EX: Quero analisar os dados dos passageiros do Titanic, disponíveis como um arquivo CSV:

Importando_CSV = pd.read_csv(r"C:\Users\Josue\Documents\Projetos Github\public_knowledge_base\Python\Projetos Pessoais\Pandas\vendas.csv")
# Read para inportar a planilia.

# PRATICANDO ALGUNS COMANDOS QUE JA APRENDI:
    
    # print(Importando_CSV) = Exibir o arquivo
    # print(Importando_CSV.max()) = Maximo de alhuma coluna
    # print(Importando_CSV.describe()) # discrição de alguma coluna
    # print(Importando_CSV["Produto"]) # Filtrar uma coluna

# EXEMPLOS DE SITUAÇÕES:

# Quero ver as primeiras 8 linhas de um DataFrame do pandas:

# Para ver as primeiras N linhas de um DataFrame, use o head()método com o número necessário de linhas (neste caso 8) como argumento.
    # print(Importando_CSV.head(2)) = ver quantidades de linhas x que o usiario determinar. começando de cima para baixo.
# se o usuario solicitar as ultimas linhas (sentido de baixo para cima) temos que utilizar:
    #print(Importando_CSV.tail(2))


# EXEMPLOS DE SITUAÇÕES:

# verificar como o pandas indentificou cada tipo de coluna, se é: inteiros ( int64), flutuantes ( float64) e strings ( object). vamos usar
    #print(Importando_CSV.dtypes)


# EXEMPLOS DE SITUAÇÕES:

# Meu colega solicitou os dados do Titanic em uma planilha:

print(Importando_CSV.to_excel("testeExel.xlsx", sheet_name="vendas02", index=False)) 
print(Importando_CSV.head())
