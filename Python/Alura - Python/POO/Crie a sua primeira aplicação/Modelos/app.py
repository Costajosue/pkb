
# Utilizando o medoto de impotação do python
# Vamos importar os medelos restalrantes, bebidas e prato
from Modelos.Restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato

# Criando instancias dos restalrantes;
restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O Melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main(): # Função onde pedimos para exibir todos os restaurantes;
    restaurante_praca.exibir_cardapio

if __name__ == '__main__': # Definindo como nosso programa principal.
    main()