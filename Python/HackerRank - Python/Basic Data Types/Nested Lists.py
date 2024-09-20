if __name__ == '__main__':
        estudantes = []

        for _ in range(int(input())):
                nome = str(input())
                nota = float(input())
                estudantes.append([nome, nota])
        notas = sorted(set(nota for nome, nota in estudantes)) 
        menores = sorted(nome for nome, nota in estudantes if nota == notas[1])
        for i in menores:
                print(i)