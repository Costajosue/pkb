#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele 
#ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa 
#também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu no ano de {} tem {} no ano de {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voçe deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não pode se alistar, falta {} anos para voce se alistar'.format(saldo))
    ano = atual + saldo
    print('seu alistamento se em {}'.format(ano))   
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi a {}'.format(ano))