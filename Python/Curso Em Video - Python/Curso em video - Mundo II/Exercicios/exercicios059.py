'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Digite o primero número:'))
n2 = int(input('Digite o segundo número:'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Selecione uma opção:'))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é de {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamnete:')
        n1 = int(input('Digite o primero número:'))
        n2 = int(input('Digite o segundo número:'))
    elif opção == 5:
        print('FINALIZANDO...')
    else:
        print('Opção invalida tente novamente...')
    print('=+=' * 10)
    sleep(2)
print('Fim do programa... Volte sempre.')