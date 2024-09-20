#           - CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE CONPRAR.
#                                           - CONSIDERE US$ 1,00 = R$ 5.24

real = float(input('Quando dinheiro você tem na carteira R$: '))
dolar = real / 5.24
print('Com R$:{:.2f} você pode comprar U$:{:.2f}'.format(real, dolar))