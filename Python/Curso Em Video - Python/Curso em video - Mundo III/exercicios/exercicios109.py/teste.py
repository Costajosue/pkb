import moeda

p = float(input('Olá digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.dobro(p, True)}')
print(f'Aumentando em 10% temos R$: {moeda.aumentar(p, 10, True)}')