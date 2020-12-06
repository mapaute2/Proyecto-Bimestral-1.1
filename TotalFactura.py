print("Total Factura")
print("**PROGRAMA PARA CALCULAR EL VALOR TOTAL DE UNA FACTURA CON DESCUENTO**")

#Inicializacion de variables 

subtotal = float(0)
total = float(0)
descuento = float(0)
limite1 = 200
limite2 = 500

#Datos de entrada

subtotal = float(input("Ingrese el subtotal de la compra: "))
subtotal = float(subtotal)

#Proceso

if subtotal >= limite1 and subtotal < limite2:
   descuento = 0.10  
        
else:
    if subtotal >= limite2:
    	descuento = 0.15
                
total = subtotal -  (subtotal * descuento)
        
#Presenta la salida de resultados

print(" El total de la compra es " ,total , " con un descuento de " , descuento)
        