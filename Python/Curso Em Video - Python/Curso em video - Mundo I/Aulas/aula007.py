Nome = input('Qual é seu nome ?')
print(' Prazer em te conhecer {:=^20}! '. format(Nome)) 

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
# PARA AQUI ESTOU USANDO ALGUMAS DAS OPERADORES ARITMÉTICOS.
# PARA NÃO QUEBRAR A LONHA DE COD. BASTA COLOCAR END='' COMO NO EXENPLO

# print(' A soma é {}, o produto é {}, e a divisão é {:.2f}'.format(s, m, d), End = '')

# ja para quebrar a linha basta seguir o exenplo acima e adicionar o \n no local aonde quer separar.
# print(' A soma é {}, \n o produto é {}, \n e a divisão é {:.2f}'.format(s, m, d))

print(' A soma é {}, o produto é {}, e a divisão é {:.2f}'.format(s, m, d))
print(' Divisão inteira {} e potência {}'.format(di, e))