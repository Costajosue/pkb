#  Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#  Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
#  em ordem crescente.

lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print(f'o número {n}, foi cadastrado com sucesso!')
    else: 
        print(f'Valor {n} já foi adicionado ')
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':  
        print(f'Você digitou os valores:\n {sorted(lista)}')
        break
        