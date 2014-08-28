def ValorCadena(cad1,cad2):
	cad1=str(cad1)
	cad2=str(cad2)
	if(len(cad1)==len(cad2)):
		return cad1+cad2
	elif (len(cad1)>len(cad2)):
		return cad1
	else:
		return cad2
cadena1=raw_input()
cadena2=raw_input()
comparacion=ValorCadena(cadena1,cadena2)
print comparacion