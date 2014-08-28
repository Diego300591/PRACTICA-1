lista=[]
lista1=[]
print "Ingrese dos numeros, uno inicial y otro final "
num1=raw_input()
num1=int(num1)
num2=raw_input()
num2=int(num2)
if num1>num2:
	aux=num1
	num1=num2
	num2=aux
print num1
print num2
for i in range(num1,num2+1):
	lista.append(i)
print lista
for i in lista:
	if i%2==0:
		lista1.append(i)
print lista1