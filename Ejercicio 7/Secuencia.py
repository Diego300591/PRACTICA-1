num=raw_input()
num=int(num)
i=1
while i<=num:
	cad=""
	j=1
	while j<=i:
		aux=i
		dig=str(aux)
		cad=cad+dig
		j=j+1
	print cad
	i=i+1
aux1=num-1
while aux1>=1:
	cad=""
	k=aux1
	while k>=1:
		aux2=aux1
		dig1=str(aux2)
		cad=cad+dig1
		k=k-1
	print cad
	aux1=aux1-1
