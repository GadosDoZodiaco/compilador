from .TabelaSimbolos import TabelaSimbolos
from .Token import Token

class Analisador:

    IGNORAR_ESPACOS_EM_BRANCO = True

    def __init__(self) -> None:
        pass

    def extrair_tokens(self, string : str) -> TabelaSimbolos:
        tabela = TabelaSimbolos()

        if self.IGNORAR_ESPACOS_EM_BRANCO:
            string = ''.join(string.split())

        token = Token()
        for c in string:

            print(c)