n=raw_input()
n=int(n)
P=[]
cant_p=0
suma=0
i=1
while cant_p<n:
	div=0
	for j in range(1,i+1):
		if(i%j==0):
			div=div+1
	if div==2:
		P.append(i)
		cant_p=cant_p+1
		suma=suma+i
	i=i+1
print "Los numeros primos son ",P
print "La suma es de ",suma


