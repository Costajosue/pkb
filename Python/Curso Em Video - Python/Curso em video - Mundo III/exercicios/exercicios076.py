listagem = ('Borracha', 2.00, 
        'caderno', 15.90,
        'livro', 10.90,
        'mochila', 59.99,
        'estojo', 29.99 )
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end= '')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
