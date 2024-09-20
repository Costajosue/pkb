# escreva um programa que leia um valor em metros e a exiba convertido em centimetro e milimetros.
# primeiramente temos que criar as variaveis

medida = float(input('Uma distancia em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

# aqui eu coloquei todas as medidas, agora vamos para a parte de executar essas medidas.

print('a medida de {} m corresponde a {} km e {} hm e {} dam'.format(medida, km, hm, dam))
print('tendo em vista que {} m tambem significa {} dm {} cm e {} mm'.format(medida, dm, cm, mm))



