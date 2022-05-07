import matplotlib.pyplot as plt
import numpy as np
import time

def q(x):
    return np.cos(x) - x

def q_linha(x):
    return -np.sin(x) - 1

# Método da bisseção
def bissecao(f, a, b, tol, n_max):
	i = 1
	aproxs = []
    
	while i <= n_max:
		p = (a + b) / 2.0
		Fa = f(a)
		Fp = f(p)
  
		aproxs.append(p)

		if (Fp == 0) or ((b - a) / 2.0) < tol:
			return aproxs
		elif Fa * Fp > 0:
			a = p
		else:
			b = p
   
		i += 1
	
	print("O Método falhou apos {} iteracoes\n".format(n_max))
	return -999999

# Método de Newton
def newton(f, f_linha, p0, tol, n_max):
    i = 1
    aproxs = [p0]
    
    while i < n_max:
        
        p = p0 - ((f(p0)) / (f_linha(p0)))
        aproxs.append(p)
        if abs(p - p0) < tol:
            
            return aproxs
        
        p0 = p
        i += 1
        
    print("O metodo falhou apos {} iteracoes".format(i))
    return -999999

# Calcula o desempenho dos métodos da bisseção e de Newton e retorna a sequência de
# aproximações de cada um
def desenpenhoMetodos(f, f_linha, a, b, p0, tol, n_max):
    
    t0_bissec = time.time()
    aproxs_bissec = np.array(bissecao(f, a, b, tol, n_max))
    tf_bissec = time.time()
    t_bissec = (tf_bissec - t0_bissec) * 1000
    
    t0_newton = time.time()
    aproxs_newton = np.array(newton(f, f_linha, p0, tol, n_max))
    tf_newton = time.time()
    t_newton = (tf_newton - t0_newton) * 1000
    
    return [[t_bissec, aproxs_bissec], [t_newton, aproxs_newton]]

# Plota o gráfico de f e as aproximações obtidas em desempenhoMetodos()
def plotF(f, f_linha, a, b, p0, tol, n_max, dt):
    
    result_bissec, result_newton = desenpenhoMetodos(f, f_linha, a, b, p0, tol, n_max)
    bissec_x = result_bissec[1]
    bissec_y = f(bissec_x)
    
    newton_x = result_newton[1]
    newton_y = f(newton_x)
    
    x = np.linspace(a, b, dt)
    y = f(x)
    
    plt.figure()
    plt.subplot(121)
    plt.plot(x, y, 'k', bissec_x, bissec_y, 'bo')
    plt.plot(x, x * 0, 'k--')
    plt.xlabel("Pn")
    plt.ylabel("f(Pn)")
    plt.title("Método da Bisseção")
    
    plt.subplot(122)
    plt.plot(x, y, 'k', newton_x, newton_y, 'ro')
    plt.plot(x, x * 0, 'k--')
    plt.title("Método de Newton")
    plt.xlabel("Pn")
    plt.ylabel("f(Pn)")
    
    plt.show()
    
# Teste da função plotF    
plotF(q, q_linha, 0, 2 * np.pi, np.pi / 4, 0.0001, 100, 100)