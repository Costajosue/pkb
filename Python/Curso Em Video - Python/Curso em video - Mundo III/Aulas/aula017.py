#  Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
#  As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
#  acessíveis por chaves individuais.



#           PARA ADICIONAR ELEMENTOS EM UMA LISTA:
# Lista.append(" ex ") -> Para add na lista...
# Lista.insert('0, 19')  -> para add em um local esquisito.


#           PARA APAGAR ALGUNS ELEMENTOS:
#  del['']
#  .pop()
#  .removel()


#            CRIAR LISTAS ATRAVEZ DE RANGE:
# valores = lista(range(4, 11)) -> criando uma lista de 4 a 10

#            ORGANIZAR OS ITEIS DA LISTAS 
# .sort()
# .sort(reverse=True)


# len() --> quantos elementos tem nas listas

num = [2, 5, 9, 1]
num[2] = 3    # -> para mudar na lista 
num.append(7) # -> para add na lista
# num.sort()   -> para organizar a lista
num.sort(revarse=True) # -> outro metodo para organizar
num.insert(2, 2) # -> add valores em um ponto expecifico 
# num.pop(2) # -> para eliminar elemento ou vc pode usar o 
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4 !')
print(num)
print(f'Essa lista tem {len(num)} elementos') # -> qd elemetos tem...

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} ')
print('fim')   
