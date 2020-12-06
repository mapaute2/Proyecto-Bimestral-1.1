print("Edad de una persona")
print("**PROGRAMA PARA DETERMINAR LA EDAD DE UNA PERSONA EN AÑO, MES Y DÍA**")

#Inicializacion de variables 

MesActual = 1
DiaActual = 1
AñoActual = 1
DiaNacimiento = 1
MesNacimiento = 1
AñoNacimiento = 1
edadAños = 1
edadMeses = 1
edadDia = 1

#Datos de entrada

DiaActual = int(input(" Escribe el día actual: "))

MesActual = int(input(" Escribe el mes actual: "))

AñoActual = int(input(" Escribe el año actual: "))

DiaNacimiento = int(input(" Escribe el día de nacimiento: "))

MesNacimiento = int(input( " Escribe el mes de nacimiento: "))

AñoNacimiento = int(input(" Escribe el año de nacimiento: "))

edadDia = DiaActual - DiaNacimiento
edadMeses = MesActual - MesNacimiento
edadAños = AñoActual - AñoNacimiento

# Proceso

if edadDia < 0:
	edadMeses = edadMeses - 1
	edadDia = edadDia + 30

if edadMeses < 0:
	edadAños = edadAños - 1
	edadMeses = edadMeses + 12

# Salida de resultados

print("Tu edad es: " ,edadAños , " años con " ,edadMeses , " meses y " ,edadDia , " días")

