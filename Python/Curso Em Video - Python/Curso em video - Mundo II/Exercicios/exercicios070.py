total = totimil = menor = cont = 0
barato = ''
while True:
    Produto = str(input('Qual o nome do produto: '))
    preço = float(input('Preço: '))
    total += preço
    cont += 1
    if preço > 1000:
        totimil += 1
    if cont == 1:
        menor = preço
        barato = Produto
    else:
        if preço < menor:
            menor = preço
            barato = Produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer comtinuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou')
print(f'O total e de R$: {total:.2f}')
print(f'Temos {totimil} produtos com o valor mais de R$: 1000 reais...')
print(f'O menor preço o produto {barato} custa R$: {menor:.2f}')