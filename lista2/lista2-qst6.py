import library as lib
import numpy as np

def f(x):
    return np.cos(np.exp(x) - 2) - (np.exp(x) - 2)

def f_linha(x):
    return -np.exp(x) - np.exp(x) * np.sin(np.exp(x) - 2)

def g(x):
    return x**2 - 4*x + 4 - np.log(x)

def g_linha(x):
    return 2*x - 4 - (1/x)

def h(x):
    return 2*x*np.cos(2*x) - (x + 1)**2

def h_linha(x):
    return -4*x*np.sin(2*x) + 2*np.cos(2*x) - 2*x - 2

def j(x):
    return x - 0.8 - 0.2 * np.sin(x)

def j_linha(x):
    return 1 - 0.2 * np.cos(x)

# (a) [0.5, 1.5]
lib.plotF(f, f_linha, 0.5, 1.5, 0.001, 100, 100)
lib.plotTempoExec(f, f_linha, 0.5, 1.5, 100)

# (b) [1, 2]
# lib.plotF(g, g_linha, 1, 2, 0.001, 100, 100)
# lib.plotTempoExec(g, g_linha, 1, 2, 100)

# (c) [-3, -2]
# lib.plotF(h, h_linha, -3, -2, 0.001, 100, 100)
# lib.plotTempoExec(h, h_linha, -3, -2, 100)

# (d) [0, pi/2]
# lib.plotF(j, j_linha, 0, np.pi / 2, 0.001, 100, 100)
# lib.plotTempoExec(j, j_linha, 0, np.pi / 2, 100)

# (e) ???