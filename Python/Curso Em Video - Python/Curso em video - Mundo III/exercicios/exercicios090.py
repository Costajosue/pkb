# Exercício Python 090: 
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Nota'] = float(input('Nota: '))

if dicionario['Nota'] >= 5:
    print('Aprovado!')
else:
    print('Reprovado!')

'''----------------------------------------------------------------------------------------------------------------'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media do aluno {aluno["Nome"]} :  '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovados'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['sitiação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

