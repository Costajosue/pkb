# Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h. mostre uma mensagem
# ddizendo que ele foi multado. A multa vai custar R$: 7,00 por cada km acima do limite.

velocidade = float(input('Qual a sua velocidade ?'))
print('Analizando...')
if velocidade<= 80:
    print('muito bem! voçe esta na velocidade certa')
else:
    print('VOÇE FOI MULTADO! TENHA MAIS ATENÇÃO!')
    multa = (velocidade -80) *7
    print('voce devera pagar um multa de R$: {:.2f}'.format(multa))
print('tenha um otimo dia !')    

