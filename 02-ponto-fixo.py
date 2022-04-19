import math
import matplotlib.pyplot as plt
import numpy as np

def g(x):
    return x


def pontoFixo(p0, tolerancia, numMax):
    i = 1
        
    while i <= numMax:
        print(p0)
        p = g(p0)
        
        if abs(p - p0) < tolerancia:
            return p
        
        p0 = p
        i += 1
    
    print("O Metodo falhou apos {} iteracoes\n".format(i))

print(pontoFixo(1.5, 0.0000001, 1000))