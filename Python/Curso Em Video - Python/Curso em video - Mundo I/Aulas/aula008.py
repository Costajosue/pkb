#                                                    UTILIZAÇÃO DE MODULOS.
# Na video aula o professor explica que podemos fazer e criar muito mais o que o proprio python pode fazer originalmente por isso,
# ele encina que podemos importar pacotes de funçoes para facilitar na hora de escrevermos uma linha.
#        para isso usamos o comando import (nome do pacote)


import math

# como vimos esse é o comando, logo abaixo temos un exenplo da funçao sqrt que significa: raiz e assim não precisamos sinais para culcular raiz.
# ja caso vc queira importar apenas uma funcionalidade do pacote vc tera que usar: 

from math import (funcionalidade)

num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format)(num, raiz)
