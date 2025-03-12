# # Istalar as Bibliotecas: dash, pandas e openpyxl. a baixo mostro como fazer um imports de cada biblioteca:

# from dash import Dash, html, dcc
# import plotly.express as px # contruir graficos
# import pandas as pd # ler base de dados 

# # Abaixo vou estar construindo um layout do Dashboard: 

# # importar a planilia com os dados:
# app = Dash(__name__)
# df = pd.read_excel("Vendas.xlsx")
# df = pd.read_excel("C:\Users\Josue\Documents\Projetos Github\public_knowledge_base\Python\Projetos Pessoais\Vendas.xlsx")

# def Criando_grafico():
#     fig = px.bar(df, x="Produtos", y="Quantidades", color="ID Loja", barmode="group")
#     opcoes = list(df['ID Loja'].unique())
#     opcoes.append("Todas as Lojas")