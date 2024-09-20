import moeda

p = float(input('Olá digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10% temos R$: {moeda.moeda(moeda.aumentar(p, 10))}')