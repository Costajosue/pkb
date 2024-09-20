# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TCLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA 
# EX: DIGITE UM NUMERO: 6127
# O MUMERO 6127 TEM A PARTE INTEIRA 6
from math import trunc
num = float(input('Digite um numero:'))
print('o valor digitado foi {} e a sua porção é {}'.format(num, trunc(num)))