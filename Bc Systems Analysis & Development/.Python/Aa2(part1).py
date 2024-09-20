# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor
# ímpar. Imprima os três vetores.

print('Olá seja bem vindo')
usuario = str(input('Qual o seu Nome: '))
print(f'Olá Sr(a): {usuario}. Seja bem vindo!')


vetor = [[], []] # Aqui criamos a lista "vetor" onde criei outras duas listas que vou nomar de par(posição 0) e inpar(posição 1)
valores = 0 

for c in range(1, 21): # Aqui estou pedindo para a linha 12 rpde 20 vezes atravez dp for range
    valores = int(input('Para começarmos, Digite um numero: ')) # Aqui estou pedindo para que o usuario digite nos numeros =

    if valores % 2 == 0: # se a (valores que o usuario digitou for % por 2, isso que dizer que ele e par sendo assim: )
        vetor[0].append(valores)  # se o valor for par add ele na lista( vetor [0])

    else:
        vetor[1].append(valores)#(Se ele não for divisivel por 2 ele não e par e sim impar entao ele sera add na lista (vetor [1])

print('-=' *30)# organizar/dividir       

vetor[0].sort() # usando o comando sort para organizar de forma cresente os numeros nas listas 
vetor[1].sort()
vetor.sort()

print(f'Os valores PARES são: {vetor[0]} ')# pedindo para p/ o computador escrever o resultado que armazenamos nas listas acima.
print('-=' *30)# organizar/dividir 
print(f'OS valores IPARES são: {vetor[1]} ')
print('-=' *30)# organizar/dividir 
print(f'todos os valores digitados são: {vetor}')
print('-=' *30)# organizar/dividir 
print('FIM!')

