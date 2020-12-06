print("Conversión Metros")
print("***Conversion de metros a centimetros, kilometros, pies y pulgadas***")

#Inicialización de variables 

C = float(0)
M = float(0)
K = float(0)
PI = float(0)
PU = float(0)

#Lectura de datos

M = float(input(" Ingresar el valor en metros: "))
M = float(M)

#Proceso

C = (M*100)/1
K = (M*1)/1000
PI = (M*1)/0.3048
PU = (M*39.37)/1

#Salida de resultados

print(" El valor en centímetros es : %.5f" %C)
print(" El valor en kilómetros es: %.5f" %K)
print(" El valor en pies es: %.5f" %PI)
print(" El valor en pulgadas es: %.5f" %PU)



