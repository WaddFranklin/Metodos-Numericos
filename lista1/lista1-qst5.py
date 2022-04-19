'''
    --------------------------------------------------------------------
    Universidade Federal de Alagoas - UFAL
    Instituto de Computação - IC
    Curso de Ciência da Computação
    --------------------------------------------------------------------
    Aluno: Waddinsohn Franklin dos Santos Nascimento
    Matrícula: 16111121
    Disciplina: Métodos Numéricos
    1a Lista de Exercícios - Questão 5
    Descrição: Implemente uma função que receba um número com a precisão padrão
    do Python, e plote o gráfico de erro relativo, onde o eixo horizontal representa
    a quantidade de digitos a qual o número será truncado, e o eixo vertical re-
    presenta o erro relativo. Varie a quantidade de digitos de truncamento entre
    1 e 10, em cada um dos itens da segunda questão.
    --------------------------------------------------------------------
'''
from decimal import *
import math
import matplotlib.pyplot as plt

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

def calculaPontosGraf(real):
    x = []
    y = []
    i = 1
    while i <= 10:
        x.append(i)
        normal, n = formaNormal(real)
        trunc = truncamento(normal, n, i)
        y.append(erroRelativo(real, trunc))
        i += 1
    return [x, y]

plt.figure()

# letra (a) 10 ** pi
x, y = calculaPontosGraf(math.pi)
plt.subplot(221)
plt.plot(x, y, 'ro')
plt.title("(a) 10^pi")
plt.xlabel("Quantidade de dígitos do truncamento")
plt.ylabel("Erro Relativo")

# letra (b) 2^(0.5)
x, y = calculaPontosGraf(math.sqrt(2.0))
plt.subplot(222)
plt.plot(x, y, 'ro')
plt.title("(b) 2^(0.5)")
plt.xlabel("Quantidade de dígitos do truncamento")
plt.ylabel("Erro Relativo")

# letra (c) e^10
x, y = calculaPontosGraf(math.e**10)
plt.subplot(223)
plt.plot(x, y, 'ro')
plt.title("(c) e^10")
plt.xlabel("Quantidade de dígitos do truncamento")
plt.ylabel("Erro Relativo")

# letra (d) 8!
x, y = calculaPontosGraf(math.factorial(8))
plt.subplot(224)
plt.plot(x, y, 'ro')
plt.title("(d) 8!")
plt.xlabel("Quantidade de dígitos do truncamento")
plt.ylabel("Erro Relativo")

plt.show()

