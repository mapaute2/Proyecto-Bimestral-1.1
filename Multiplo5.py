print(" Multiplo de 5")
print("***PROGRAMA QUE MUESTRE LOS NÚMEROS MÚLTIPLOS DE 5 DE 0 A 100***")

#Inicializacion de variables

n = 100
multiplo = 5
i = 0

print("BUCLE (FOR)")

#Ciclo

for i in range (1,n+1):
	if i % multiplo == 0:
		print(i)


