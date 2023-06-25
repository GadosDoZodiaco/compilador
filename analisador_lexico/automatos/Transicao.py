from .Estado import Estado
from ..Token import Token
from .AutomatoTokenGenerico import AutomatoTokenGenerico

class Transicao:
    origem_label : str
    tipo : AutomatoTokenGenerico
    destino_label: str

    def __init__(self, origem : str, tipo : AutomatoTokenGenerico, destino : str) -> None:
        self.origem_label = origem
        self.destino_label = destino
        self.tipo = tipo