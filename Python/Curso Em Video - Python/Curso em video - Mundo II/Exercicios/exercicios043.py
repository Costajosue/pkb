#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso (KG)?'))
altura = float(input('Qual a sua altura?'))
IMC = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Voçe esta abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('parabens voçe esta no peso ideal!')
elif 25 <= IMC < 30:
    print('voçe esta com um sobrepeso!')
elif 30 <= IMC < 40:
    print('voçe esta com Obsedade')
elif IMC >= 40:
    print('voce esta com OBSIDADE MORBIDA')

