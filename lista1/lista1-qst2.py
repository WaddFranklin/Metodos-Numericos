'''
    --------------------------------------------------------------------
    Universidade Federal de Alagoas - UFAL
    Instituto de Computação - IC
    Curso de Ciência da Computação
    --------------------------------------------------------------------
    Aluno: Waddinsohn Franklin dos Santos Nascimento
    Matrícula: 16111121
    Disciplina: Métodos Numéricos
    1a Lista de Exercícios - Questão 2
    Descrição: Implemente algoritmos para calcular o erro absoluto e o erro relativo
    das aproximações de p por p*
    --------------------------------------------------------------------
'''

import math

# Cálculo do erro Absoluto
def erroAbsoluto(numero, aproximacao):
    return numero - aproximacao


# Cálculo do erro relativo
def erroRelativo(numero, aproximacao):
    return abs(erroAbsoluto(numero, aproximacao)) / abs(numero)


# Letra (a) p = 10^pi, p* = 1400
print("(a) - Erro Absoluto = {} ; Erro Relativo = {}\n".format(erroAbsoluto(10**math.pi, 1400.0), erroRelativo(10**math.pi, 1400.0)))

# Letra (b) p = 2^(0.5), p* = 1.414
print("(b) - Erro Absoluto = {} ; Erro Relativo = {}\n".format(erroAbsoluto(math.sqrt(2.0), 1.414), erroRelativo(math.sqrt(2.0), 1.414)))

# Letra (c) p = e^10, p* = 22000
print("(c) - Erro Absoluto = {} ; Erro Relativo = {}\n".format(erroAbsoluto(math.e**10, 22000.0), erroRelativo(math.e**10, 22000.0)))

# Letra (d) p = 8!, p* = 39900
print("(d) - Erro Absoluto = {} ; Erro Relativo = {}".format(erroAbsoluto(math.factorial(8), 39900), erroRelativo(math.factorial(8), 39900)))