from .Estado import Estado
from .Transicao import Transicao
from ..Token import Token
from .AutomatoTokenGenerico import AutomatoTokenGenerico

class Automato:

    _estados : list[Estado] = []

    def estado(self, label : str, final = False):
        self._estados.append(Estado(label, final))

    def estados(self, labels : list[str], finais : list[str] = []):
        for label in labels:
            final = False
            if finais.count(label):
                final = True                
            self.estado(label, final)
        
    def transicao(self, origem_label : str, tipo : AutomatoTokenGenerico, destino_label: str):
        estado_origem = None
        estado_destino = None

        def _estados_validos():
            return (estado_origem != None) and (estado_destino != None)

        for estado in self._estados:
            if estado.label == origem_label: 
                estado_origem = estado
            if estado.label == destino_label: 
                estado_destino = estado
            if _estados_validos():
                break
        
        if _estados_validos():            
            estado_origem.transicao(tipo, estado_destino)
        
    def transicoes(self, transicoes : list[Transicao]):
        for transicao in transicoes:
            self.transicao(
                transicao.origem_label, 
                transicao.tipo, 
                transicao.destino_label
            )
        
    def reconhecer(self, test : str) -> bool:

        estado = self._estados[0]
        for token in test:
            prox_estado = estado.proximo_estado(token)
            if prox_estado != None:
                estado = prox_estado
            else:
                return False
        
        return estado.final



    
