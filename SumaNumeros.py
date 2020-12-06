print(" Suma de números ")
print("**PROGRAMA PARA CALCULAR LA SUMA DE UNA SERIE DE NÚMEROS**")

# Inicialización de variables 

i = 0
n = 0
suma = 0

# Pedir que se ingrese el limite de los números

n = int(input(" Ingrese el límite de números a presentar: "))
n = int(n)

# Iniciamos el ciclo repetitivos while

while i <= n:
	suma = suma + i
	i = i + 1 

print(" La suma de los números es: " ,suma)

