# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero:'))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num , c, num*c))
