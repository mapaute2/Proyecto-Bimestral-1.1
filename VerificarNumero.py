print(" Verificar Número")
print("**PROGRAMA PARA VERIFICAR SI UN NÚMERO ES PAR O IMPAR Y REALIZAR SU SUMA**")

#Inicializacion de variables 

cont = 1
n = 1
num = 0
sumPar = 0
sumImpar = 0
sumPosi = 0
sumNega = 0

#Datos de entrada

n = int(input(" Ingrese el límite de número a verificar: "))

#Crear el ciclo para verificar los números

while cont <= n:

	num = int(input( " Ingrese el número a verificar: "))

	if num % 2 == 0:
		sumPar = sumPar + num

	else:
		sumImpar = sumImpar + num

	if num > 0:
		sumPosi = sumPosi + num

	else:
		sumNega = sumNega + num

	cont = cont + 1

print(" La suma de los pares es: " ,sumPar)
print(" La suma de los impares es: " ,sumImpar)
print(" La suma de los positivos es: " ,sumPosi)
print(" La suma de los negativos es: " ,sumNega)
