'''
    --------------------------------------------------------------------
    Universidade Federal de Alagoas - UFAL
    Instituto de Computação - IC
    Curso de Ciência da Computação
    --------------------------------------------------------------------
    Aluno: Waddinsohn Franklin dos Santos Nascimento
    Matrícula: 16111121
    Disciplina: Métodos Numéricos
    1a Lista de Exercícios - Questão 3
    Descrição: Suponha que p* deva aproximar p com erro relativo máximo de 10^(-3) .
    Determine o maior intervalo no qual p* pode estar para os valores de p
    --------------------------------------------------------------------
'''

ERRO_RELATIVO = 10**(-3)

# Calcula os limites do intervalo de p*
def intervalo(numero, erroRelativo):
    a = -numero * (erroRelativo - 1)
    b = numero * (1 + erroRelativo)
    if a < b:
        return [a, b]
    return [b, a]

# Letra (a) p = 250
intv = intervalo(250.0, ERRO_RELATIVO)
print("(a) {} <= p* <= {}\n".format(intv[0], intv[1]))

# Letra (b) p = 25
intv = intervalo(25.0, ERRO_RELATIVO)
print("(b) {} <= p* <= {}\n".format(intv[0], intv[1]))

# Letra (c) p = 2.5
intv = intervalo(2.5, ERRO_RELATIVO)
print("(c) {} <= p* <= {}\n".format(intv[0], intv[1]))

# Letra (d) p = -0.25
intv = intervalo(-0.25, ERRO_RELATIVO)
print("(d) {} <= p* <= {}".format(intv[0], intv[1]))