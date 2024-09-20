# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')    
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso que ele É UM NUMERO PRIMO!')
else:
    print('E por isso que ele NÂO È UM PRIMO!')    