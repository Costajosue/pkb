
# n = int(input())  # Ler o número de elementos na tupla

# # Ler os inteiros separados por espaços utilizando o split() para separar estou utilizando a função map() para que 
# # Dentro da minha tupla todos os input() sejar transformados em um numero inteiro.
# t = tuple(map(int, input().split())) 

# # Calculando a hash
# hash_n = hash(t)

# print(hash_n)


n = int(input())
t = (map(int, input().split())) 

t2 = tuple(t)

print(hash(t2))