#Titulo:Determina si el estudiante Aprobo o Desaprovo

#Entrada:
#   tri1: Solicita el primer lado del triangulo
#   tri2: Solicita el segundo lado del triangulo
#   tri3: Solicita el tercer lado del triangulo

#Salida:

#Proceso:

#Solicita lado 1,
#Solicita lado2,
#Solicita lado3
tri1 = (int)(input("Ingrese el valor de lado a:"))
tri2 = (int)(input("Ingrese el valor de lado b:"))
tri3 = (int)(input("Ingrese el valor de lado c:"))

#Determina que tipo de triangulo es
if tri1 == tri2 == tri3:

#Mostrar resultado
    print("Las medidas corresponden a un triangulo equilatero")
elif tri1 == tri2 or tri1 == tri3 or tri2 == tri3:
    print("Las medidas corresponden a un triangulo isosceles")
else:
    print("Las medidas corresponden a un triangulo escaleno")