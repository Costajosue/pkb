# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, 
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os valores são {f1}, {f2} e {f3}')

# Outro exemplo

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par (num):
    print('é par!')
else:
    print('Não é par!')