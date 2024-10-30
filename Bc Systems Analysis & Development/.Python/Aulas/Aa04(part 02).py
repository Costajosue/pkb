
#-------------------------------ATIVIDADE 02-----------------------------------------------------
import pandas as pd
# import numpy as pd
print('-=' * 30)
tabela = pd.Series(data= [4, 7, 8, -2,], index=['a', 'b', 'c', 'd'])
media = tabela.mean() # para calcular a media
multi = (tabela * 2 )  # para calculcular a multiplicação entre os valores
indice = tabela['a'] # para pegar apenas o indice que a At04 pediu
print(tabela)
print('-=' * 30)
print(f'A multiplicação entre eles será de\n{multi}')
print(f'A media da tela é de {media}')
print(f'O valor no qual o índice é a letra A é {indice}')
