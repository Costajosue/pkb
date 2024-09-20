#  Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#  O programa será interrompido quando o número solicitado for negativo.


while True:
    n = int(input('Olá, digite um número para ver a tabuada: '))
    if n < 0:
            break
    for c in range (1, 11):
        print(f'{n} X {c} = {n*c}')
print('Programa Encerrado!')        

