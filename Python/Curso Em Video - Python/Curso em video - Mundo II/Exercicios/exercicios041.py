#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de 
#nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('O atleta é MIRIM')
elif idade <=14:
    print('O atleta é INFANTIL')
elif idade <=19:
    print(' O atleta é JÙNIOR ')    
elif idade <=25:
    print('O atleta e SÈNIOR')    
else:
    print('O atlrta é MASTER')    