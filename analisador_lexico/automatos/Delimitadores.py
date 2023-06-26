class Delimitadores:

    SOMA                = '+'
    SUBTRACAO           = '-'
    MULTIPLICACAO       = '*'
    DIVISAO             = '/'

    ATRIBUICAO          = '='

    PONTO_VIRGULA       = ';'
    PARENTESES_ESQUERDO = '('
    PARENTESES_DIREITO  = ')'   

    def delimitadores() -> list[str]:
        return [
            Delimitadores.SOMA, 
            Delimitadores.SUBTRACAO,
            Delimitadores.MULTIPLICACAO,
            Delimitadores.DIVISAO,
            Delimitadores.ATRIBUICAO,
            Delimitadores.PONTO_VIRGULA,
            Delimitadores.PARENTESES_ESQUERDO,
            Delimitadores.PARENTESES_DIREITO
        ]