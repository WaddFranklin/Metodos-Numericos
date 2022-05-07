import time
import numpy as np

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

res_bissec, res_newton = desenpenhoMetodos(q, q_linha, 0, 7, np.pi / 4, 0.0001, 100)

print("--- Bisseção ------------------------------")
print(f"Tempo de Execução        : {res_bissec[0]} ms")
print(f"Sequência de aproximações: {res_bissec[1]}")
print("-------------------------------------------")
print()
print("--- Newton --------------------------------")
print(f"Tempo de Execução        : {res_newton[0]} ms")
print(f"Sequência de aproximações: {res_newton[1]}")
print("-------------------------------------------")

