print("Calculadora")
print("**CALCULADORA DE OPERACIONES BÁSICAS**")

#Inicializacion de variables

num1 = float(0)
num2 = float(0)
repsuesta = float (0)
opcion = 1

#Datos de entrada

num1 = float(input("Ingrese el valor del número 1: "))
num1 = float(num1)

num2 = float(input("Ingrese el valor del número 2: "))
num2 = float(num2)

#Escriba el menú de opciones en pantalla

print(" 1. Suma")
print(" 2. Resta")
print(" 3. Multiplicación")
print(" 4. División")

opcion = int(input(" Escoja una de las siguientes opciones: "))
opcion = int(opcion)

#Se realiza la calculadora con las operaciones básicas

if opcion == 1:
	suma = num1 + num2
	print(" La suma es " ,suma)

if opcion == 2:
	resta = num1 - num2
	print(" La resta es " ,resta)

if opcion == 3:
	multiplicacion = num1 * num2
	print(" La multiplicación " ,multiplicacion)

if opcion == 4:
	división = num1 // num2
	print(" La división es " ,división)


