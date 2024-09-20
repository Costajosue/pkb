# FAÇA UM PROGRAMA QUE LEIA UMA ANO QUALQUER E MOSTRE SE ELE E BISSEXTO
ano = int(input('Que ano quer analizar? :'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO É BISSEXTO'.format(ano))    