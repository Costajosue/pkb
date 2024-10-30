import pandas as pd  
import matplotlib.pyplot as plt #importando a biblioteca 

# Dados passado pela atividade 
dados = { 
'X': [1,2,3,4,5,6],
'Y1': [120,110,130,145,118,125],
'Y2': [95,54,86,77,90,81]
}



df = pd.DataFrame(data=dados) # transformando em uma DataFrame
# print(df)

# Criando um gráfico
plt.plot(df) 

# Atribuindo um título ao gráfico 
plt.title('Exemplo utilizando Atividade 04')
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 2')

plt.show()