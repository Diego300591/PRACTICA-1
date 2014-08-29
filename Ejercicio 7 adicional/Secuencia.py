num=raw_input()
num=int(num)
for i in range(0,num):
	cad="" 
	aux=i+1
	for j in range(0,aux):
		dig=str(aux)
		cad=cad+dig
	print cad
val=num-1
while val>=1:
	cad=""
	aux1=val
	for k in range(0,aux1):
		dig=str(aux1)
		cad=cad+dig
	print cad
	val=val-1
