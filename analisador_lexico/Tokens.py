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

    def __init__(self) -> None:
        super().__init__()

    def is_delimitador(self, delimitador : str) -> bool:
        return (
            delimitador == self.VIRGULA or
            delimitador == self.PONTO_VIRGULA
        )


