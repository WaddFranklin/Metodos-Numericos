import math
import numpy as np

def h(x):
	return (x**3) + 4*(x**2) - 10

def q(x):
    return np.cos(x) - x

def q_linha(x):
    return -np.sin(x) - 1

# Método de Newton
def newton(f, f_linha, p0, tol, n_max):
    i = 1
    
    while i < n_max:
        print(p0)
        
        p = p0 - ((f(p0)) / (f_linha(p0)))
        
        if abs(p - p0) < tol:
            
            return p
        
        p0 = p
        i += 1
        
    print("O metodo falhou apos {} iteracoes".format(i))
    
# Método da bisseção
def bissecao(f, a, b, tol, n_max):
	i = 1

	while i <= n_max:
		p = (a + b) / 2.0
		Fa = f(a)
		Fp = f(p)
  
		print(p)

		if (Fp == 0) or ((b - a) / 2.0) < tol:
			return p
		elif Fa * Fp > 0:
			a = p
		else:
			b = p
   
		i += 1
	
	print("O Método falhou apos {} iteracoes\n".format(n_max))
	return -999999

# Teste para o método da bisseção
bissecao(h, 1, 2, 0.0001, 20)

# Pular uma linha
print("-------------------------------")

# Teste para o método de Newton
p0 = np.pi / 4
newton(q, q_linha, p0, 0.00000001, 1000)
