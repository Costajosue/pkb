salario = float(input('Qual o salario do funcionario:'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quam ganhava {} agora ganhara {}'.format(salario, novo))