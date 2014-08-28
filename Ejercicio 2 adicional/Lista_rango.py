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
while num1<=num2:
	lista.append(num1)
	num1=num1+1
print lista
for i in lista:
	if i%2==0:
		lista1.append(i)
print lista1