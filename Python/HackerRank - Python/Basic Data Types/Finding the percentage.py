# codigo pre definido pela situação problema:
if __name__ == '__main__':
    n = int(input())
    student_marks = {} # dicionario
    for _ in range(n):
        name, *line = input().split() # notas dos estudantes
        # usa o operador de desempacotamento (*). Isso significa que a primeira parte da lista resultante é atribuída à variável name, e o restante da lista é atribuído à variável line.
        scores = list(map(float, line)) 
        student_marks[name] = scores # adc no dicionario
    alunos_notas = student_marks[input()] # nome 

# Resolvendo o problema:
# Calculando a soma e dividindo pelo número de alunos e assim achando a media:

    media = sum(alunos_notas) / len(alunos_notas)
    resultado = "{:.2f}".format(media)

    # print(resultado)
    print(resultado)



# Documentoção lidas para resolver:

# https://awari.com.br/python-aprenda-a-trabalhar-com-duas-casas-decimais/#:~:text=Em%20Python%2C%20podemos%20arredondar%20n%C3%BAmeros,
# n%C3%BAmero%20de%20casas%20decimais%20desejado.&text=Nesse%20exemplo%2C%20o%20n%C3%BAmero%203.14159,casas%20decimais%2C%20resultando%20em%203.14.

# https://www.alura.com.br/artigos/entendendo-o-desempacotamento-no-python