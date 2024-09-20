#   Exercício Python 057: 
#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto

Sexo = str(input('Olá, digite seu sexo: [M/F]')).strip().upper()[0] # -> aqui colocamos o N° 0 para fazer um fatiamento, podendo assim pegar somente a primeira letra da pelavra digitada.
while Sexo not in 'MmFn':
    Sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(Sexo))    