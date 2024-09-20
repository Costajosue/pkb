#   Exercício Python 060: 
#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
#   Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#   Temos varios modos de resolver esse exercicios:

from math import factorial
n = int(input('Digite um número:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))   

#-----------------------------------------------------------------------#

n = int(input('Digite um número:'))
c = n
f = 1
print('Calculando ... {} !'.format(n), end='')
while c > 0:
    print('{}'.format(n), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f*= c
    c-= 1 
print('{}'.format(f))    
