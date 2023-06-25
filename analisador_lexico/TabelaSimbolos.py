from .Token import Token

class TabelaSimbolos:
    
    NUMBER_OF_TOKENS = 0

    data : list[(int, Token, int)] = []

    def __init__(self) -> None:
        pass

    def proximo_identificador(self) -> int:
        self.NUMBER_OF_TOKENS += 1
        return len(self.data)

    def adicionar(self, label: str, token : int):
        proximo_identificador = self.proximo_identificador()
        self.data.append((proximo_identificador, label, token))

    def table(self):

        print("Tabela de simbolos: ")
        for (id, label, token) in self.data:
            print(f'ID: {id} LABEL: {label}  TOKEN: {token}')
