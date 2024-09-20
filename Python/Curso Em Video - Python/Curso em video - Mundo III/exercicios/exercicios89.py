# Exercício Python 089: Crie um programa que leia nome e duas 
# notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno 
# individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar: [S/N]'))
    if resp in 'Nn':
        break

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('mostrar notas de qual aluno? (aparte 999 para finalizar)')) 
    if opc == 999:
        print('finalizado!')   
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') 
print('ACABOU')


