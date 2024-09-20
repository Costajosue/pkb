# Importando biblioteca 'OS' que nesse caso vamos utilizar para curtomizar nosso def finalizar_app(): para limpar o terminal quando optarmos pela opção de finaliza o programa\sair mostrar somente 'Finalizando programa' .
import os

restaurantes =[{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
               {'nome':'Pizza Suprema', 'categoria':'Brasileiro', 'ativo':True}, 
               {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] # criando uma Dicionario onde vamos armazenar os dados.

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗2
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opçoes(): # Criando menu do projeto:
    # Criando menu do projeto:
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurantes')
    print('4. Sair\n')


# Definindo uma função finalizar_app() para finalizar o programa na linha 34, e assim deixar o codigo mais limpo.
def finalizar_app():
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu inicial ')
        main() #chamando função main 

def opcao_invalida(): #caso o usuario não digite uma das opções ja determinadas
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): # com essa função vamos otimizar o codigo ao exibir subtitulos nas outras funções.
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante(): #Função que ira cadastrar os restaurantes;
    exibir_subtitulo('Cadastro de novos restaurantes ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}# criando dicionario
    restaurantes.append(dados_do_restaurante) # adicionando ao dicionario principal
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes(): # função que ira listar os restaurantes
    exibir_subtitulo('Listando restaurantes')

  
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes: # significa 'Para cada restaurante em restaurentes'
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' # utilizando ternario
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # .ljust(20) para dar espaços entre as informações
    voltar_ao_menu_principal()


def alternar_estado_restaurante(): #Função para Ativar e Desativar restaurante
    exibir_subtitulo('Alternado estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:# se o restaurante digitado estiver dentro do dicionario:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # se restaurante estiver ativo ele desativara pois e 'not' ira inverter sua condição 
           # utilizando metodo Ternario:
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():# Deixando o menu funcional armarzenando o input em uma variavel e logo após mestramos o resultado com o print:
    try: # significa (tente) tente executar isso:
        # Adicionando o int na frete de input significa que estamos mostrando que vamos receber um número inteiro.
        opcao_escolhida = int(input('Escolha uma opção: ')) 

        # Agora utilizando o if, elif e else para colocarmos funcionalidades nas opções.
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: # caso não consiga:
        opcao_invalida()


def main():# função para limpar ou voltar para o menu de interação;
    os.system('cls') #comando para limpar a tela/terminal
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opcao()

if __name__ == '__main__':
    main() 