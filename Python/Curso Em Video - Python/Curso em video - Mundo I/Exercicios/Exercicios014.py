#    ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM c graus E CONVERTA EM f graus

c = float(input('Informe a temperatura em ºc:'))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºc corresponde a {}ºF!'.format(c, f))