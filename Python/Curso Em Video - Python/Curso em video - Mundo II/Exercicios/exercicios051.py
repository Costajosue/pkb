# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('primeiro termo: '))
razão = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razão #(FORMULLA DO ENECIMO DE UMA PA)
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')    