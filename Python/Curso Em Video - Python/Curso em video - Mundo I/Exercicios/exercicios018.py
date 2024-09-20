# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TAMGENTE DESSE ANGULO
import math
angulo = float(input(' Digite o angulo que voçe deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print(' o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tamgente = math.tan(math.radians(angulo))
print(' O angulo {} tem a tanguente de {:.2f}'.format(angulo, tamgente ))