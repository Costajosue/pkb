# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
# acessíveis por chaves literais.

# Como criar um dicionário em Python?
# Para iniciar um dicionário em Python, você precisa definir a variável e colocar os valores entre chaves {}.

# De um lado, com as aspas, pode-se definir a chave específica; do outro, o valor associado. Cada par é separado por vírgulas.

# Fica mais ou menos assim:

dic = {'Nome': 'josue'}


# metodos 
# Keys() (para obter as chaves do dicionário).
# método Values (para obter os valores do dicionário)

# Método Keys e Método Values
# O método Keys é usado para retornar todas as chaves do meu dicionário. O formato de retorno é uma lista comum. 
# Ao passo que o método Values retorna todos os valores em uma lista também.
# Isso é muito útil quando se quer apenas um lado das informações da tabela, uma versão enxuta. Permite que o programador explore o dicionário como uma lista comum para fins específicos.
# Ou seja, os dicionários não somente são ótimos como uma forma de enriquecer a visão sobre os dados, como também podem ser convertidos em formas mais simples de organização. São, portanto, versáteis. 

# Como adicionar e remover informações do dicionário Python? 
# Lembrando que, para adicionar um novo elemento ao dicionário, se usa:
# dic[“a” ] = variável
# Aí você está inserindo nessa chave “a” o valor da variável.
# Para remover, você pode usar os métodos que já mencionamos. Relembrando: o pop permite remover um item especificado. O popitem remove aleatoriamente um item de qualquer ordem.