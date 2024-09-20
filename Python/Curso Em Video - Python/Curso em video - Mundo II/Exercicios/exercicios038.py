""" Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:"""

"""– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

#------------------------------------------------------------------------------------------------------------------------------------

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
print('Comparando...')
if num1 > num2:
    print('O primeiro valor e maior ')
elif num1 < num2:
    print(' O segundo valor e maior ')
else: 
    print('Não exixte valor maior, os dois são iguais. ')
