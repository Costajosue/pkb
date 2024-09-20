# AULA SOBRE CONDIÇÕES ANINHADAS.

nome = str(input('Qual é seu nome?'))
if nome == 'Gustavo':
    print('Seu nome é incrivel!')
elif nome == 'pedro' or nome == 'maria':
    print('Seu nome é muito normal aqui no Brasil') 
elif nome == 'josue':
    print('Ola, meu amigo')
else:
    print('Seu nome é norma!')    
print('Tenha um otimo dia {}'.format(nome))



