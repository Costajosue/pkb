# FAÇA UM PROGRAMA QUE LEIA A LARGUARA E A ALTURA DE UMA PAREDE EM METROS E CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA 
#SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2 m2

# vamos ver as medidas da parede 
# númeors float 

larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print(' sua parede tem a dimensão de {} x {} e a sua area e de {} m2 '.format(larg, alt, area))
tinta = area / 2 
print(' para pintar essa parede vc gastara {}L de tinta'.format(tinta))