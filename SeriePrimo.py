print(" Serie Primo")
print("**PROGRAMA PARA GENERAR LA SERIE**")

#Inicializacion de variables 

n = 0
num = 0
den = 0
suma = 0
primo = 2
divisor = 0
cont = 0
j = 1

n = int(input("Programa para generar la serie \nIngrese el limite de la serie\n"))

for i in range(1,(n+1)):
    num = i
    cont = 0

    while cont == 0:
       den = den + 1
       j = 1
       for j in range(j, (den+1)):
            if den % j == 0:
                divisor = divisor + 1
       if divisor == 2:
            cont = 1
       divisor = 0
    if i % 2 == 0:
        print (i, " -", +num, " / ", den)
    else: 
        print(i, " +", num, " / ", den)
    suma = suma + ((-1) **(i+1))*(num/den)                    
print("------------------------------")
print(f'La suma de la serie es: {suma}')