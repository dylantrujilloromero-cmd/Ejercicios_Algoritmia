#Titulo:Determina si la persona es usuario o administrdor

#Entrada:
#   ad1: Solicita el rol

#Salida:

#Proceso:

#Pide registrarse
ad1 = (input("Ingrese su rol (admin/usuario)"))

#Reconoce y Ejecuta según su rol 
if ad1 == "admin":

#Mostrar el resultado
    print("Acceso como admin permitido")
else:
    print("Acceso como usuario permitido")