from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')) # criando uma variavel para nome
nasc = int(input('Ano de nascimento: ')) # Criando uma variavel parea termos o ano de nascimento
dados['idade'] = datetime.now().year - nasc # Para calcular a idade do usuario impotamos a biblioteca (datetime), assim podemos pegar o ano atual e subitrair com o ano de nascimento para assim achar a sua idade...
dados['ctps'] = int(input('Carteira de trabalho: ')) # Variavel para achar a certeira de trabalho;
# caso o usuario digite o numero 0 o programa para e encerra.
if dados['ctps'] != 0: # porém se ele digitar o numero da sua ctps....
    dados['Contratação'] = int(input('Data de contratação: '))# aparce a variavel data da sua primeira contratação.
    dados['salario'] = float(input('Salario; R$'))# variavel salario.
    dados['aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)# Aqui vamos calcular a aposentadoria do usuario
    # pegando a variavel idade que achamos mais a cima e somamos com a data da contratação + 35Anos o logo - pelo ano atual do usuario...
for k, v in dados.items():# Aqui vamos apenas arrumar para ficar mais limpa nossa resposta...
    print(f'{k} tem o valor {v}')
