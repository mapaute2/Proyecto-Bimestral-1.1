print(" Serie Fibonacci ")
print("**PROGRAMA PARA IMPRIMIR NÚMEROS EN SERIE**")

#Inicializacion de variables 

n = 0
primero = 0
segundo = 1
fibo = 0
i = 0
suma1 = 0

#Datos de entrada

n = int(input(" Ingrese el límite de la serie Fibonacci: "))
print("\n")

#Ciclo 

for i in range (1,n):
	if i < 2:
		print(i , "," ,primero)
		print(i + 1, ", " ,segundo)
		suma = primero + segundo 
		i = i + 1
	else:
		fibo = primero + segundo
		suma = suma + fibo
		primero = segundo 
		segundo  = fibo

		print(i , ", " ,fibo)

print("\n La suma total:" ,suma)
print ("Segunda solucion")

primero = 0 
segundo = 1 
fibo = 0
for i in range (1,n+1):
	print (i , " ," ,primero)
	suma1 = suma1 + primero
	fibo = primero + segundo
	primero = segundo
	segundo = fibo
print ("\n La suma total:" ,suma1)



