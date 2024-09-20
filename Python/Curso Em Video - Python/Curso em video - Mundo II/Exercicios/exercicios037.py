# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero:'))
print('''Escolha um opção:
[1] binario
[2] octal
[3] hexadecimal''' )
opção = int(input('Selecione uma opção: '))
if opção == 1:
    print('O numero {} convertido para binario fica {}'.format(numero, bin(numero)[:2])) # [:2] = tecnica de fatiamento...
    print('O numero {} convertido para actal fica {}'.format(numero, oct(numero)[:2]))
elif opção == 3:
    print('O numero {} vai ficar {} em hexadecimal'.format(numero, hex(numero)[:2]))
else:
    print('Opção incorreta!')


