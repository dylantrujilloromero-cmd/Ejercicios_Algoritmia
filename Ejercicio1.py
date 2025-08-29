#entradas:
#   nombre: El nombre del usuario
#   apellido: El apellido del usuario

#salidas:
#   iniciales: La primera letra de Nombre y Apellido

#Proceso: Pedir al usuario su nombre y apellido, y mostrar sus iniciales en mayuscula


#Pedir al usuario su nombre y apellido
nombre = input ("Ingrese su nombre:")
apellido = input ("Ingrese su apellido")

#Tomar la primera letra de cada variable y convertirla a mayuscula
iniciales = nombre[0].upper + apellido [0].upper()

#Mostrar el resultado
print("Tus iniciales son:", iniciales)