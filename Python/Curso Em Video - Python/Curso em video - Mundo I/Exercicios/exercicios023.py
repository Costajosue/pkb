#faça um programa que leia os numeros de 0 a 9999 e mostre na tela cada um dos digitos separados 
#ex:
#unidade:
#dezena:
#milhar:

num = int(input('Ola digite um numero: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('analisando o numero: {}'.format(num))
print('unidade; {}'.format(uni))
print('dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))