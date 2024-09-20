teste = list()
teste.append('Josue')
teste.append('18')
galera = list()
galera.append(teste[:]) # -> [:] é utilizado para fezer uma copia...
teste[0] = 'leandro'
teste[1] = 22
galera.append(teste[:])
print(galera)

#      Outra Forma de declarar :

galera = [['Josue', 18],['leandro', 22],['Maria', 19],['Yasmin', 34]]
print(galera[0] [1])

#------------------------------------------------------------------------

galera = [['Josue', 18],['leandro', 22],['Maria', 19],['Yasmin', 34]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#------------------------------------------------------------------------

# Agora voms ver um exenplo onde criamos 2 listas uma principal e outra secundaria e vamos armazenar
# as informações temporariamente e,m uma e logo passar para a principal e logo vaoms excluir a outra...

galera = list()
dado = list()
totmaio = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ! ') 
        totmaio += 1
    else:
        print(f'{p[0]} é menor de idade ! ')
        totmenor += 1

print(f' Temos {totmaio} maiores e {totmenor} menores de idade.')        