#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual será a sua jogada ?'))
print('-=' * 17)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 17)
 #projeto em andamento...