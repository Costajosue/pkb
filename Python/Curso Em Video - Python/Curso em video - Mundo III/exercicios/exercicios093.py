# Exercício Python 093: 
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('   olá qual o nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["Nome"]} jogou ?  '))
for c in range(0, partidas):
    partidas.append(int(input(f' Quantos gols na partida {c}'))) 
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'o jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["total"]):
    print(f'   Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

