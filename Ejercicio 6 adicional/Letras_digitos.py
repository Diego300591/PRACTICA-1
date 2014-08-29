cad=raw_input()
cad=str(cad)
i=0
tam=len(cad)
tam=int(tam)
letras=0
digitos=0
while i<tam:
	if(cad[i]>='a' and cad[i]<='z') or (cad[i]>='A' and cad[i]<='Z'):
		letras=letras+1
	elif cad[i]>='0' and cad[i]<='9':
		digitos=digitos+1
	i=i+1
print "letras: ",letras
print "digitos: ",digitos