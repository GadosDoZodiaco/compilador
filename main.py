from analisador_lexico import Analisador
from analisador_lexico.automatos import Automato, Transicao, AutomatoTokenGenerico


# analisador = Analisador()
# analisador.extrair_tokens("a = b + c;")

# Automato para reconhecer variavel
automato_reconhece_variavel = Automato()
automato_reconhece_variavel.estados(labels=["q1", "q2"], finais=["q2"])
automato_reconhece_variavel.transicoes(transicoes=[
    Transicao("q1", AutomatoTokenGenerico.LETRA, "q2"),
    Transicao("q2", AutomatoTokenGenerico.LETRA, "q2"),
    Transicao("q2", AutomatoTokenGenerico.DIGITO, "q2"),
])

# Automato para reconhecer
automato_reconhece_numero = Automato()
automato_reconhece_numero.estados(labels=["q1", "q2", "q3"], finais=["q2", "q3"])
automato_reconhece_numero.transicoes(transicoes=[
    Transicao("q1", AutomatoTokenGenerico.DIGITO, "q2"),
])


print("Aceito: ", automato_reconhece_numero.reconhecer("a"))
