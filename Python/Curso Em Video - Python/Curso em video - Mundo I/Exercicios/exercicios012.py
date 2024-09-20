# FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.

preço = float(input('Qual é o preço do produto? R$:'))

# vemos que na linha de cima pedimos para o usuario revelar o preço original do produto, para que assim na linha inferior possamos calcular
# o novo preço usando o o sinbulo de ( / ) para divisão e o de ( * ) para multiplicação e assim fazer o preço * 5% de 100.

novo = preço - (preço * 5 / 100) 
print('O produto que custava {:.2f}, com o super desconto de 5% custara apenas R$:{:.2f}'.format(preço, novo))

