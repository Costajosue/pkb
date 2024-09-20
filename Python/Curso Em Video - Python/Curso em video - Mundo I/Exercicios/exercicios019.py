# FAÇA UM PROGRAMA QUE AJUDE UM PROFESSOR A SORTEAR 1 ALUNO ENTRE 4
import random
n1 = str(input(' Escreva o primeiro nome: '))
n2 = str(input(' Escreva um segundo nome: '))
n3 = str(input(' Escreva o terceiro nome: '))
n4 = str(input(' Escreva o quarto numero: '))
Lista = [n1, n2, n3, n4]
escolhido = random.choice(Lista)
print(' o escolhido é: {}'.format(escolhido))
