# Importando uma biblioteca para metodos abstratos
from abc import ABC, abstractmethod

# Criando uma classe para os itens do cardapio. Juntamente com um construtor __Init__ com as informações base que teremos na classe.
class ItemCardapio:
    def __init__(self,nome,preco):
        self._nome = nome # -> colocando o _ para indicar que esses valores e esclusivo do item_cardapio.
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass