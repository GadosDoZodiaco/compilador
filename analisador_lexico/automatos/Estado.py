from ..Token import Token
from analisador_lexico.automatos import Estado
from .AutomatoTokenGenerico import AutomatoTokenGenerico

NUMERO_DE_ESTADOS = 0

class Estado:
    
    cod : int
    label : str
    final : bool
    transicoes : dict[AutomatoTokenGenerico, Estado]

    def __init__(self, label : str, final = False) -> None:
        self.label = label
        self.final = final
        self.transicoes = {}


    def transicao(self, tipo : AutomatoTokenGenerico, estado : Estado):
        self.transicoes[tipo.value] = estado

    def proximo_estado(self, consumivel : str):       
        tipo = AutomatoTokenGenerico.tipo(consumivel)
        if tipo.value in self.transicoes:
            return self.transicoes.get(tipo.value)
        else:
            return None
        


        

            
            
            
            