# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO. CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA 
import math 
co = float(input(' Qual o comprimento do cateto oposto: '))
ca = float(input(' qual o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(' A hipotenusa vai medir {:.2f}'.format(hi))