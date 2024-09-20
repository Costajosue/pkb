distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua viagem ficara no valor de R$:{:. 2f}'.format(preço))       
