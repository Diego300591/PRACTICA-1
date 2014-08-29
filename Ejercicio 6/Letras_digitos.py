cad=raw_input()
cad=str(cad)
letras=0
digitos=0
for i in cad:
	if (i>='a' and i<='z')or(i>='A' and i<='Z'):
		letras=letras+1
	elif(i>='0' and i<='9'):
		digitos=digitos+1
print "letras: ",letras
print "digitos: ",digitos