#                              Curso Python #10 - Condições (Parte 1)
# ESTRUTURA CONDICIONAL SIMPLES:

nome = str(input('Qual é seu nome? '))
if nome == 'josue':
    print('Bem vindo chefe! ') 
print('tenha um otimo dia: {}'.format(nome))    

# ESTRUTURA CONDICIONAL CONPOSTA: 

nome = str(input('Qual é seu nome? '))
if nome == 'josue':
    print('Bem vindo chefe! ')
else:
    print('acesso negado! ')   
print('tenha um otimo dia: {}'.format(nome))    

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print('sua nome sera {:.1f}'.format('m'))
if m>= 6.0:
    print('sua nota foi ecelente! PARABENS!')
else:
    print(' Sua nota foi ruim ESTUDE MAIS!')

