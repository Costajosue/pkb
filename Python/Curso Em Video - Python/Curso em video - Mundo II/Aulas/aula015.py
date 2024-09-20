# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. 
# É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

n = s = 0
while True: # -> estara em lup infinito...
    n = int(input('Digite um número: '))
    if n == 999:
        break # --> significa 'Parada'
    s += n
print('A soma vale {}'.format(s))    

# Aprendi também uma nova forma de usar o .format
# chamdo F strings:

# print(f'A soma vale {s}') # -> usamos o 'f' minusculo no inicio da string e a variavel logo após...