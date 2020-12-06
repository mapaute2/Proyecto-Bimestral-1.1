print("Potencia Número")
print("**Programa para sacar la potencia de un número**")

#Inicializacion de variables 

base = 0
pot = 0
cont = 1
result = 1

#Datos de entrada

base = int(input(" Ingresar la base de la potencia: "))

pot = int(input(" Ingresar la potencia: "))

#Ciclo repetitivo que obtine la potencia de un número

while cont <= pot:
	result = result * base
	cont = (cont + 1)

print(" La potencia de: " ,base, " elevado a " ,pot, " es " ,result)
