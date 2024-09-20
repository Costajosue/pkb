# FAÇA UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
# - QUANTOS VEZES APARECE A LETRA "a"
# - EM QUE POSIÇÃO ELA APARECE A PRIMEIRA LETRA 
# - EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

frase = str(input(' Ola seja bem vindo, Digite uma frase: ')).upper() # usamos o upper para jogar tudo para maiusculo e assim imdentificar toas as letras A
print('A letra A aparece {} veses na frase'.format(frase.count('A')))
 # usamos o count para indentificar somente a letra A na frase

print('A primeira letra A aparece na posição: {}'.format(frase.find('A')+1))
# ja aqui nos utilizamos o find para encontras a primeiraou ou a primeira posiçao da letra ou palavra de uma frase.

print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))
# utizando o rfind para indentificar somente no lado direito a ultima letra.