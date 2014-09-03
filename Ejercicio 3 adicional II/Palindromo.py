def es_palindromo(cadena):
	cadena=str(cadena)
	longitud=len(cadena)
	longitud=int(longitud)
	tam=longitud-1
	cadena1=""
	resultado=""
	while tam>=0:
		cadena1=cadena1+cadena[tam]
		tam=tam-1
	if cadena1==cadena:
		resultado=True
	else:
		resultado=False
	return resultado
cad=raw_input("Ingrese una cadena ")
aux=es_palindromo(cad)
print aux

