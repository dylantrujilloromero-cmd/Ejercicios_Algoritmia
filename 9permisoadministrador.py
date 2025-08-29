#Titulo:Ingrese como administrador

#Entrada:
#   contra1: Solicita la contraseña

#Salida:

#Proceso:

#Pide contraseña
contra1 = (float)(input("Ingrese la contraseña de administrador"))

#Determinar si validando la contraseña ingresa como administrador
if contra1 == 2222:

#Mostrar resultado
    print("Acceso permitido como administrador")
else:
    print("Ingreso denegado")