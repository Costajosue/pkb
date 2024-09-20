from exercicios115.lib.interface import *
from exercicios115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
   criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastrada', 'Cadastrar Novas Pessoas' ,' Sair do Sitema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome:'))
        idade = leiaInt('idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até Logo!')
        break
    else:
        print('ERRO! Digite um número valido! ')
    sleep(2)