import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**3) + 4*(x**2) - 10

'''
	Recebe uma função f, um intervalo [a, b] e um passo dt
	Output = Gráfico da função f de a até b sendo [a, b] dividido em dt subintervalos
'''
def plotF(f, a, b, dt):
    x = np.linspace(a, b, dt)
    y = f(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
    
# Teste da função plotF
plotF(f, -10, 10, 100)