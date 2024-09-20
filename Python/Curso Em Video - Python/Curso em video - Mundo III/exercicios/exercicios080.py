# Exercício Python 080: 
# Crie um programa onde o usuário possa digitar cinco valores numéricos ok
# e cadastre-os em uma lista, ok
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    v = int(input('Digite um numero: '))
    if c == 0:
        lista.append(v)
    elif c > lista[len(lista)-1]:
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos,v)
                break
            pos += 1
print(f'os valores digitados em ordem foram {lista}')



