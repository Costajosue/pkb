# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python 
# e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote, 
# ampliando ainda mais a modularização em grandes projetos em Python.

from Pacotes import numeros


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}. ')

print(f'dobro de {num} é {numeros.dobro(num)}')

