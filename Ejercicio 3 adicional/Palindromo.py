def es_palindromo(cadena):
	cadena=str(cadena)
	longitud=len(cadena)
	longitud=int(longitud)
	tam=longitud-1
	cadena1=""
	while tam>=0:
		cadena1=cadena1+cadena[tam]
		tam=tam-1
	if cadena1==cadena:
		print True
	else:
		print False
cad=raw_input("Ingrese una cadena ")
aux=es_palindromo(cad)

