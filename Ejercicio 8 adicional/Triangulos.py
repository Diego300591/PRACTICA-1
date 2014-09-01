import math
def triangulo(a,b,c):
	if((a+b)>c)and((a+c)>b)and((b+c)>a):
		if a==b and a==c and b==c:
			return "Es triangulo equilatero"
		elif a==c and b!=c and a!=b:
			return "Es triangulo isoceles"
		elif c==(math.sqrt(a**2+b**2)):
			return "Es triangulo rectangulo"
		else:
			return "Es triangulo escaleno"
	else:
		return "No es triangulo"
a=raw_input()
a=float(a)
b=raw_input()
b=float(b)
c=raw_input()
c=float(c)
calculo=triangulo(a,b,c)
print calculo