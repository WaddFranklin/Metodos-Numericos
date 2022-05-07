import numpy as np
import random
import matplotlib.pyplot as plt
import time

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

# Método de Newton adaptado para gerar um p0 aleatório em (a, b) caso não convirja
def newtonV2(f, f_linha, a, b, tol, n_max):
    i = 0
    max_attempts = 10
    aproxs = []
    
    for j in range(max_attempts):
        p0 = random.uniform(a, b)
        aproxs.append(p0)
            
        while i < n_max:
            print(p0)
            p = p0 - (f(p0) / f_linha(p0))
            aproxs.append(p)
            
            if abs(p - p0) < tol:
                return aproxs
            
            p0 = p
            i += 1
        i = 0
        
    print("O método falhou após {} tentativas!".format(max_attempts))
    
# Calcula o desempenho dos métodos da bisseção e de Newton e retorna a sequência de
# aproximações de cada um
def desenpenhoMetodos(f, f_linha, a, b, tol, n_max):
    
    t0_bissec = time.time()
    aproxs_bissec = np.array(bissecao(f, a, b, tol, n_max))
    tf_bissec = time.time()
    t_bissec = (tf_bissec - t0_bissec) * 1000
    
    t0_newton = time.time()
    aproxs_newton = np.array(newtonV2(f, f_linha, a, b, tol, n_max))
    tf_newton = time.time()
    t_newton = (tf_newton - t0_newton) * 1000
    
    return [[t_bissec, aproxs_bissec], [t_newton, aproxs_newton]]

# Plota o gráfico de f e as aproximações obtidas em desempenhoMetodos()
def plotF(f, f_linha, a, b, tol, n_max, dt):
    
    result_bissec, result_newton = desenpenhoMetodos(f, f_linha, a, b, tol, n_max)
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
    
# 
def plotTempoExec(f, f_linha, a, b, n_max):
    i = 1
    x = []
    t_bissec = []
    t_newton = []
    while i < 21:
        x.append(2**(-i))
        i += 1
        
    for i in x:
        result_bissec, result_newton = desenpenhoMetodos(f, f_linha, a, b, i, n_max)
        t_bissec.append(result_bissec[0])
        t_newton.append(result_newton[0])
        
    y_bissec = np.array(t_bissec)
    y_newton = np.array(t_newton)
    
    plt.figure()
    plt.plot(x, y_bissec, 'b', x, y_newton, 'r')
    plt.xlabel("Tolerância")
    plt.ylabel("Tempo de execução (ms)")
    plt.title("Tolerância x Tempo de Execução")
    plt.show()
