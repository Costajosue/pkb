#     # CORES

# # print('\033[1;36;41m ola, mundo!')

# #      # SEMPRE DEVEMOS USAR O COMANDO \033[M 
# #      # SE OPITAR POR COLORIR SOMENTE AS PALAVRAS DEVEMOS USAR:
# # print('\033[1;36;41m ola, mundo!\033[m]')

# #-------------------------------------------------------------------------------------

# a = 3
# b = 4
# print('Os valores são\033[32m {}\033[m e \033[31m{}\033[m!'.format(a, b))

# #-------------------------------------------------------------------------------------

# nome = 'josué'
# print('olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

 #-------------------------------------------------------------------------------------
nome = 'josué'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))