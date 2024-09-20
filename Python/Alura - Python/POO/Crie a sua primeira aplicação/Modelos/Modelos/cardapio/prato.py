# importar o cardapio
from Modelos.cardapio.item_cardapio import ItemCardapio

# Criando a clesse prato do nosso restaurante.
class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco) # Super = utilizamos para acessar as informções de outra classe.
        
        # como herdamos 'nome' e 'preço' da classe cardapio, vamos apenas criar a descrição.
        self.descricao = descricao

    #Criar uma representação de texto do Objeto:
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)