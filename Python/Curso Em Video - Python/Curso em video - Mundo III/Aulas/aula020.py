# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos


# ex:
#def mostrarLinha():
#    print('---------------------------')
    
# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')


# # Programa principal:
# soma(b=4, a=5)
# soma(7, 2)

# def contador(*num):
#     for valor in num:
#         print(f'{valor} ',end='')
#     print('Fim!')


# contador(2, 1, 7)
# contador(8, 2)
# contador(4, 4, 7, 6, 2)


# def contador(*num):
#      tam = len(num)
#      print(f'Recebi os valores {num} e são todos {tam} números')


# contador(2, 1, 7)
# contador(8, 2)
# contador(4, 4, 7, 6, 2)


# def soma(* valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'somando os valores {valores} temos {s}')


# soma(5, 2)
# soma(2, 9, 4)
