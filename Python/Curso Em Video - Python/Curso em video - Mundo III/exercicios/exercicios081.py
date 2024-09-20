'''Exercício Python 081: 

- [ ]  Crie um programa que vai ler vários números e colocar em uma lista.

 Depois disso, mostre:

- [ ]  A) Quantos números foram digitados.
- [ ]  B) A lista de valores, ordenada de forma decrescente.
- [ ]  C) Se o valor 5 foi digitado e está ou não na lista '''

Lista = []
while True:
    n = int(input('Digite um número: '))
    Lista.append(n)
    d = str(input('Deseja comtinuar? [S/N]: '))
    if d in 'N':
        break
Lista.sort(reverse=True)    
print(f'Você digitou: {len(Lista)} elementos')
print(f'os números são: {Lista}')
if 5 in Lista:
     print('O valor 5 está na lista !')
else: 
    print('O valor 5 não está na Lista !')
