# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno com as dimenções {largura}X{comprimento} é de {a}m2')


print('controle de terrenos:')
print('-' *20)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(l, c)