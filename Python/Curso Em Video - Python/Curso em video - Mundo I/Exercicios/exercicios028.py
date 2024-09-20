'''escreva um programa que faça o computador 
'pensar' em um numero inteiro entre 0 e 5 e
peça para o usuario tentar descobrir qual 
foi o numero escolhido pelo computador. o
programa devera escrever se o usuario venceu ou não '''

from random import randint
computador = randint(0, 5) # ESSE COMANDO FAZ O COMPUTADOR PENSAR EM UM NUMERO DE 0 A 5 
print(' PENSANDO... {}'.format(computador))
print('-/-' * 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-/-' * 20)
jogador = int(input(' Qual o numero eu pensei ?:'))
if jogador == computador:
    print(' muito bem! voçe acertou! ')
else:
    print('HAHAHA voçe perdeu! Eu pensei no numero {} e não no {}'.format(computador, jogador))


