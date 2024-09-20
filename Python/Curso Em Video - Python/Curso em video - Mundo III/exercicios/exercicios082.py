'''Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo 
das três listas geradas.'''

lista = []
par = []
impar = []
while True:
    n = int(input(' Digite um número por favor: '))
    lista.append(n)
    if n %2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input('Deseja digitar mais números ? [S/N]: ')).upper()[0]
    if resp == 'N':
        break
print(f'você digitou os numeros: {lista}')
print(f'Sendo par os números: {par}')
print(f'E os inpar são {impar}')