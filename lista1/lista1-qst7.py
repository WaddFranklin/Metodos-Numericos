'''
    --------------------------------------------------------------------
    Universidade Federal de Alagoas - UFAL
    Instituto de Computação - IC
    Curso de Ciência da Computação
    --------------------------------------------------------------------
    Aluno: Waddinsohn Franklin dos Santos Nascimento
    Matrícula: 16111121
    Disciplina: Métodos Numéricos
    1a Lista de Exercícios - Questão 7
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

def f(x):
    return 1.01*(x**4) - 4.62*(x**3) - 3.11*(x**2) + 12.2*x - 1.99

def fAninhada(x):
    return x*(12.2 -x*(3.11 + x*(4.62 - 1.01*x))) - 1.99

real = f(4.62)
aninhado = fAninhada(4.62)

print("f(1.53)         = {}".format(real))
print("fAninhada(1.53) = {}".format(aninhado))