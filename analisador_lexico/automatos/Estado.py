from ..Token import Token
from analisador_lexico.automatos import Estado
from .AutomatoTokenGenerico import AutomatoTokenGenerico

class Estado:
    
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
        


        

            
            
            
            