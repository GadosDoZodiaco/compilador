from analisador_lexico import Analisador, Tokens, TabelaSimbolos
from analisador_lexico.automatos import Automato, Transicao, AutomatoTokenGenerico, Delimitadores


# analisador = Analisador()
# analisador.extrair_tokens("a = b + c;")

def automato_variavel():

    # Automato para reconhecer variavel
    automato_reconhece_variavel = Automato(Tokens.IDENTIFICADOR)
    automato_reconhece_variavel.criar_estados(labels=["q1", "q2"], finais=["q2"])
    automato_reconhece_variavel.transicoes(transicoes=[
        Transicao("q1", AutomatoTokenGenerico.LETRA, "q2"),
        Transicao("q2", AutomatoTokenGenerico.LETRA, "q2"),
        Transicao("q2", AutomatoTokenGenerico.DIGITO, "q2"),
    ])
    
    return automato_reconhece_variavel

def automato_numero():
    
    # Automato para reconhecer
    automato_reconhece_numero = Automato(Tokens.NUMERO)
    automato_reconhece_numero.criar_estados(labels=["q1", "q2"], finais=["q2"])
    automato_reconhece_numero.transicoes(transicoes=[
        Transicao("q1", AutomatoTokenGenerico.DIGITO, "q2"),
        Transicao("q2", AutomatoTokenGenerico.DIGITO, "q2"),
    ])

    return automato_reconhece_numero


def teste_reconhecer_expressao():


    automatos = [
        automato_variavel(),
        automato_numero()
    ]

    expressao = "a = b + 22; a = c + b"

    expressao_recortada = []
    token = ""
    for c in expressao:
        if c in Delimitadores.delimitadores():
            recorte = token[:expressao.index(c)].strip()
            expressao_recortada.append(recorte)
            token = ""
        else:
            token += c

    tabelaSimbolos = TabelaSimbolos()
    for token in expressao_recortada:     
        for automato in automatos:
            aceito = automato.reconhecer(token)
            if aceito:
                tabelaSimbolos.adicionar(token, automato.tipo)
            print(f'Automato({automato.tipo})\t{token}\t[{aceito}]')
    tabelaSimbolos.table()


teste_reconhecer_expressao()
