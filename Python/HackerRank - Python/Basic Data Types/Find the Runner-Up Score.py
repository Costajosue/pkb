# Encontrar o segundo colocado #


if __name__ == '__main__':
    notas = []
    # imputar o valor de 'n':
    n = int(input())
    # definindo a Ponduação dos alunos e utilizando o map no lugar de uma for e a função split para colocarmos um espaço entre cada nota.
    pontuação = map(int, input().split())
    # Criando uma lista e adc as pontuações ja colocando em ordem descresente com o sort e reverse=True
    notas = list(set(pontuação)) # Utilizando a função set para excluir possiveis notas duplicadas.
    notas.sort(reverse=True)# sort para organizar em ordem e 'reverse=True' para ficar de dorma descresente.
print(notas[1])