listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
                menor = listanum[c]
print(f'Você digitou os números {listanum}')
print(f'o maior valor sera {maior} nas posições ')
for i, v in enumerate(listanum):
     if v == maior:
          print(f'{i}')
print(f'o menor valor sera {menor} nas posições  ')
for i, v in enumerate(listanum):
     if v == menor:
          print(f'{i}') 