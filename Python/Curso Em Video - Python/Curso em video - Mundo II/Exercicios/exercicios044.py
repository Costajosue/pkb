#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

##– à vista dinheiro/cheque: 10% de desconto

##– à vista no cartão: 5% de desconto

##– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros 

print('{:=^40}'.format(' LOJAS DO JOSUÉ '))
preço = float(input('Qual o valor da compra: R$'))
print(''' FORMAS DE PAGAMENTO:

[1] À VISTA DINHEIRO/ CHEGUE
[2] À VISTA NO CARTÃO 
[3] EM ATÉ 2X NO CARTÃO
[4] EM 3X OU MAIS NO CARTÃO ''')
opção = int(input(' Selecione uma opção para pagamento: '))
if opção == 1:
    total = preço - ( preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra sera parcelada em 2x de R$: {} Sem juros '.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input(' Qual o numero de parcelas:'))
    parcela = total / totalparcelas
    print('Sua compra será parcelador em {}x de R$: {:.2f} com juros'.format(totalparcelas, parcela))
else:
    total = preço
    print('opção de pagamento invalida!')
print('Sua compra de R$: {:.2f} vai custar R$:{} no final'.format(preço, total))
