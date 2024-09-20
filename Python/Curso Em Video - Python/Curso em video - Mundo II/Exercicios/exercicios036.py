#  Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário 
#ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa R$:'))
salario = float(input('Qual a sua renda por mes R$:'))
anos = int(input('Em quantos anos voçe que pagar ?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R$: {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação ficara {:.2f}'.format(prestação))
if prestação <= minimo:
    print('EMPRESTIMO LIBERADO!')
else:
    print('EMPRESTIMO NÂO DISPONIVEL!')    