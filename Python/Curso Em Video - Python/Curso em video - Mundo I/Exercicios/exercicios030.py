# crie um programa que leia um numero e diga se ele é PAR ou IMPAR.
numero = int(input('Digiti um numero:'))
resultado = numero % 2
if resultado == 0:
    print(' O numero {} e PAR'.format(numero))
else:
    print('o numero {} e IMPAR'.format(numero))  