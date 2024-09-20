# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS 
# QUIAS ELE FOI ALUGADO. CALCULE P PREÇO A PAGAR, SABENDO QUE P CARRO CUSTA R$ 60 POR DIA E R$:0.15 POR KM RODADOS.

# como vamos perguntar quantos dias o corro esta alugado e int pois e um numero inteiro. 
dias = int(input('Quantos dias alugados? '))

# agora vamos começar a misturar. e perguntar quantos km, como não sabemos se e um numero inteiro vamos de float
km = float(input('Quantos km rodados? '))


# temos que dividir esse exercicio em pedaços semdo a primeira parte um quanto a se pagar por dias e logo após incluimos km rodados 
#     CODIGO =====      pago = dias * 60 
# LOGO DEPOIS INCLUIMOS O VALOR EM KM 

pago = (dias * 60) + (km * 0.15)
print(' O total a pagar é de R$: {:.2f}'.format(pago))