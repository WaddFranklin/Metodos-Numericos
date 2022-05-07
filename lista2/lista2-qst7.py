import library as lib
import numpy as np

def f(x):
    return (np.e**x) * np.sin(x + 30) + 1

def f_linha(x):
    return (np.e**x) * (np.sin(x + 30) + np.cos(x + 30))

def g(x):
    return np.cos(x) - 2**(x - 10) + 2

def g_linha(x):
    return -np.sin(x) - 2**(x - 10) * np.log(2)

# (a) No intervalo [1, 2] f(x) possui uma raiz 
print(lib.newtonV2(f, f_linha, 1, 1.5, 0.001, 100))

# (b) No intervalo [10.5, 11.5] g(x) possui uma raiz 
# print(lib.newtonV2(g, g_linha, 10.5, 11.5, 0.001, 100))