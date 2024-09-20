from exercicios115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileExistsError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRo na criação do arquivo !')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()

def cadastrar(arg, nome='desconhecido', idade=0):
    try:
        a = open(arg, 'at' )
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dados')
        else:
            print(F'Novo registro de {nome} adicionado')
            a.close
