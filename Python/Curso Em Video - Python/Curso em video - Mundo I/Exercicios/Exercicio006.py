# Crie um algoritimo que leia um número e mostre o seu triplo, e raiz quadra
n = int(input('Digite um número: '))
d = n * 2 
t = n * 3 
r = n ** (1/2)
print('o dobro de {} vale {}. '.format(n, d))
print(' o triblo de {} vale {}. '.format(n, t))
print(' A raiz de {} e igual a {}. '.format(n, r))