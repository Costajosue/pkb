from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR?')).strip().upper()[0]
    print(f'Você joagou {jogador} e o computador {computador}; total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('PERDEU!')
            break      
    elif tipo == 'I':
        if total % 2 ==1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('VOCE perdeu')
            break
    print('Vamos jogar novamente...')  
print(f'GAME OVER! VOCÊ VENCEU {v} VEZES. ')    
    