# CEIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM ''SILVA'' EM SEU NOME

nome = str(input('Qual o seu nome?')).strip()
#   Aqui usamos o (strip) para tirar todos os espaços rncluindo os espaços quwe podem ser adcionos sem querer pelos usuarios.

print('Seu nome tem Silva ? {}'.format('SILVA' in nome.upper()))

# Usamos o operador ''in'' para indentificar somente a palavra SILVA na frase undependente de sua posição.