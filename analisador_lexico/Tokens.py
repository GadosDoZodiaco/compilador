from enum import Enum

class Tokens(Enum):

    IDENTIFICADOR       = 1
    NUMERO              = 2
    STRING              = 3

    SOMA                = 4
    SUBTRACAO           = 5
    MULTIPLICACAO       = 6
    DIVISAO             = 7

    ATRIBUICAO          = 8

    PONTO_VIRGULA       = 9
    VIRGULA             = 10
    PARENTESES_ESQUERDO = 12
    PARENTESES_DIREITO  = 13    

    def is_delimitador(delimitador : str) -> bool:
        return (
            delimitador == Tokens.VIRGULA or
            delimitador == Tokens.PONTO_VIRGULA
        )


