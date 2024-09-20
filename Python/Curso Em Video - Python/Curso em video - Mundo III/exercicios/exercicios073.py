# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times. ok

#b) Os últimos 4 colocados. ok

#c) Times em ordem alfabética. ok

#d) Em que posição está o time da Chapecoense.

tab = ('BOTAFOGO','PALMEIRAS','FLAMENGO','ATLÉTICO-MG','FLUMINENSE',
       'GRÊMIO','ATHLETICO-PR','SÃO PAULO','CRUZEIRO','INTERNACIONAL',
        'INTERNACIONAL', 'chapecoense','RED BULL BRAGANT','SANTOS','CUIABÁ','BAHIA',
        'CORINTHIANS','GOIÁS','AMÉRICA-MG','VASCO','CORITIBA')

print(f'Listas de times: {tab}')

print(f'Os primerios 5 colocados são: {tab[0: 5]}')

print(f'Os ultimos 4 da tabela são: {tab[16: 20]}')

print(f'Os times em ordem alfabetica fica: {sorted(tab)}')

print(f'O time chapecoense esta em {tab.index("chapecoense")} posição')