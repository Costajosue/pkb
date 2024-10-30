# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
# multiplicação e os números.
soma = 0 
mult = 1
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    soma += num
    mult *= num
print(f'A soma dos numeros são: {soma}')
print(f'A multiplicação dos numeros são: {mult}')
