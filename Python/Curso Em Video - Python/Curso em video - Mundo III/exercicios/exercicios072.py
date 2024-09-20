# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
        'Cinco', 'Seis', 'sete', 'Oito', 'nove',
        'Dez', 'onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte'  )
while True:
    núm = int(input('Digite um número de 0 a 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente mais uma vez,', end=' ')
print(f'Você digitou o número {cont[núm]}')
