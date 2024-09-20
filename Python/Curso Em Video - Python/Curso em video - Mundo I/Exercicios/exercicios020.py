# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATR0 ALUNOS E MOSTRE A ORDEM SORTEADA.
import random
n1 = str(input(' escreva um nome: '))
n2 = str(input(' escreva outro nome: '))
n3 = str(input(' escreva outro nome: '))
n4 = str(input(' escreva outro numero: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(' A ordem de apresentação sera:')
print(lista)