def es_palindromo(cadena):
	longitud=len(cadena)
	longitud=int(longitud)
	tam=longitud-1
	cadena1=""
	while tam>=0:
		cadena1=cadena1+cadena[tam]
		tam=tam-1
	if cadena1==cadena:
		return True
	else:
		return False
cad=raw_input("Ingrese una cadena ")
cad=str(cad)
aux=es_palindromo(cad)
print aux

