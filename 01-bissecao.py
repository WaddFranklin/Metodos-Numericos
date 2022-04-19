def f(x):
	return (x**3) + 4*(x**2) - 10

def bissecao(a, b, tolerancia, max_iteracoes):
	i = 1

	while i <= max_iteracoes:
		pt_medio = (a + b) / 2.0
		Fa = f(a)
		Fb = f(b)
		Fpt_medio = f(pt_medio)

		#print("iteracao = {}".format(i))
		#print("a = {}".format(a))
		#print("b = {}".format(b))
		print("p = {}".format(pt_medio))
		#print("F(p) = {}".format(Fpt_medio))

		if (Fpt_medio == 0) or ((b - a) / 2.0) < tolerancia:
			return pt_medio
		elif Fa * Fpt_medio > 0:
			a = pt_medio
		else:
			b = pt_medio
		i += 1
	
	print("O Método falhou apos {} iteracoes\n".format(max_iteracoes))
	return -999999


print(bissecao(1, 2, 0.0001, 20))