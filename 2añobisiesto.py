#Titulo:Determina si el año es bisiesto

#Entrada:
#   año1: Solicita el año

#Salida:

#Proceso:

#Pedir al usuario que ingrese un año
año1 = (float)(input("Ingrese el año:"))

#Toma el año y determina si el año es bisiesto
if (año1 % 4 == 0 and año1 % 100 != 0) or (año1 % 400 ==0):

#Mostrar el resultado
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")