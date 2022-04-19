import math

def f(x):
    return math.cos(x) - x

def f_linha(x):
    return (-1)*(math.sin(x)) - 1

def newton(p0, tolerancia, numMax):
    i = 1
    while i < numMax:
        print(p0)
        
        p = p0 - ((f(p0)) / (f_linha(p0)))
        
        if abs(p - p0) < tolerancia:
            
            return p
        
        p0 = p
        
    print("O metodo falhou apos {} iteracoes".format(i))
    
p0 = math.pi / 4
print(newton(p0, 0.00000001, 1000))