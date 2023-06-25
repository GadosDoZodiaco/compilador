from enum import Enum

class AutomatoTokenGenerico(Enum):

    TOKEN_NAO_RECONHECIDO = 1
    LETRA   = 2
    DIGITO  = 3


    def is_digito(token : str):
        return token.isdigit()
    
    def is_letra(token : str):
        return token.isalpha()
    
    def tipo(token : str):
        if (AutomatoTokenGenerico.is_digito(token)):
            return AutomatoTokenGenerico.DIGITO
        if (AutomatoTokenGenerico.is_letra(token)):
            return AutomatoTokenGenerico.LETRA
