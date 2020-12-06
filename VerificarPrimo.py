print(" Verificar Primo")
print("**PROGRAMA PARA VERIFICAR SI UN NÚMERO ES PRIMO**")

#Inicializacion de variables 

cont = 1
cont1 = 1
n = 1
num = 0
divisor = 0

#Datos de entrada

n = int(input(" Ingrese el límite de números a verificar si son primos: "))

while cont <= n:
	num = int(input(" Ingrese el número a verificar: "))

	while cont1 <= num:

		if num % cont1 == 0:
			divisor = divisor +1

		cont1 = cont1 + 1

	if divisor == 2:
		print(num, " es Primo ")
		print("------")

	else:
		print(num, " no es Primo")
		print("-----")

	cont1 = 1
	divisor = 0
	cont = cont +1