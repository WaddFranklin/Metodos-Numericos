'''
    --------------------------------------------------------------------
    Universidade Federal de Alagoas - UFAL
    Instituto de Computação - IC
    Curso de Ciência da Computação
    --------------------------------------------------------------------
    Aluno: Waddinsohn Franklin dos Santos Nascimento
    Matrícula: 16111121
    Disciplina: Métodos Numéricos
    1a Lista de Exercícios - Questão 4
    Descrição: Implemente algoritmos para realizar os cálculos abaixo usando trun-
    camento com 3 dígitos, truncamento com 4 dígitos, arredondamento com 3
    dígitos e arrendondamento com 4 dígitos. Realize o cálculo exato e calcule os
    erros absoluto e relativo de cada aproximação para cada item abaixo. Obs.:
    considere como cálculo exato aquele realizado em Python com sua precisão
    padrão. Você pode usar a biblioteca decimal do Python para obter apro-
    ximações dos números
    --------------------------------------------------------------------
'''
from decimal import *
import math

# Cálculo do erro Absoluto
def erroAbsoluto(numero, aproximacao):
    return abs(numero - aproximacao)

# Cálculo do erro relativo
def erroRelativo(numero, aproximacao):
    return erroAbsoluto(numero, aproximacao) / abs(numero)

# Converte um numero real para dus forma normal em ponto flutuante 
def formaNormal(numero):
    exp = 0
    while not(numero > -1 and numero < 1):
        numero /= 10
        exp += 1
    return [numero, exp]

# aplica o truncamento dados a quantidade de digitos e o numero na forma normal
def truncamento(numero, n, precisao = 0):
    exp = 10 ** (precisao)
    return (int(numero * exp) / exp) * (10 ** n)

# aplica o arredondamento dados a quantidade de digitos e o numero na forma normal
def arredondamento(numero, n, precisao = 0):
    exp = 10 ** (precisao + 1)
    numero_temp = int(numero * exp)
    ultimo_algarismo = numero_temp % 10
    
    if ultimo_algarismo >= 5:
        exp_soma = 5 * (10**((-1)*(precisao + 1)))
        numero += exp_soma
        
    return truncamento(numero, n, precisao)

# Exibe os resultados na tela
def printResultados(real):
    normal, n = formaNormal(real)
    trunc3 = truncamento(normal, n, 3)
    trunc4 = truncamento(normal, n, 4)
    arred3 = arredondamento(normal, n, 3)
    arred4 = arredondamento(normal, n, 4)
    
    print("Real:                       {}".format(real))
    print(normal, n)
    print("-------------------------------")
    print("Truncamento 3 digitos:      {}".format(trunc3))
    print("Truncamento 4 digitos:      {}".format(trunc4))
    print("Arredondamento 3 digitos:   {}".format(arred3))
    print("Arredondamento 4 digitos:   {}".format(arred4))
    print("-------------------------------")
    print("Erro Abs. Trunc. 3 digitos: {}".format(erroAbsoluto(real, trunc3)))
    print("Erro Rel. Trunc. 3 digitos: {}".format(erroRelativo(real, trunc3)))
    print("-------------------------------")
    print("Erro Abs. Arred. 3 digitos: {}".format(erroAbsoluto(real, arred3)))
    print("Erro Rel. Arred. 3 digitos: {}".format(erroRelativo(real, arred3)))
    print("-------------------------------")   
    print("Erro Abs. Trunc. 4 digitos: {}".format(erroAbsoluto(real, trunc4)))
    print("Erro Rel. Trunc. 4 digitos: {}".format(erroRelativo(real, trunc4)))
    print("-------------------------------")    
    print("Erro Abs. Arred. 4 digitos: {}".format(erroAbsoluto(real, arred4)))
    print("Erro Rel. Arred. 4 digitos: {}".format(erroRelativo(real, arred4)))
    print("")
    print("")
    

# letra (a) 133 - 0.499
real = 133 - 0.499
printResultados(real)

# letra (b) (121 - 119) - 0.327
real = (121 - 119) - 0.327
printResultados(real)

# letra (c) ((13 / 14) - (6 / 7)) / ((2 * e) - 5.4)
real = ((13 / 14) - (6 / 7)) / ((2 * math.e) - 5.4)
printResultados(real)

# letra (d) (pi - (22 / 7)) / (1 / 17)
real = (math.pi - (22 / 7)) / (1 / 17)
printResultados(real)