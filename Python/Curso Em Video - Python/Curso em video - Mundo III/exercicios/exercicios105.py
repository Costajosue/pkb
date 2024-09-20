# Exercício Python 105: 
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar 
# um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

def notas(*n, sit=False):
    """
    -> função para anslisar notas e situacões de vários alunos.
    :Para n: uma ou mais notas dos alunos (aceita várias)
    :Para sit: valor opicional, indicado se deve ou não adicionar a situação.
    :Return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'RUIM'
    return r


#PRograma principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)