import pandas as pd  
import numpy as np
dados = np.array([['Toalha', '6', 'MesaBanho'], ['Sabonete', '5', 'Perfumaria'], ['Mouse', '3', 'Informática'], ['Teclado', '2', 'Informática']])
df = pd.DataFrame(data=dados, columns=['PRODUTO', 'QNT', 'SETOR'])
print('=+'*30)
print(df)
print('=+'*30)
so_setor = df['SETOR']
print(f'Mostrando apenas o setor:  \n {so_setor }')
print('=+'*30)
compras = df[['SETOR', 'QNT']]
print(f'Quantas compras cada setor tem {compras}')