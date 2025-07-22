"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")

paises={"Mexico","Brasil","España","Canada"}
print(paises)

#Funciones u operaciones 
for i in paises:
    print(i)

paises.add("México")
print(paises)

paises.pop()
print(paises)

paises.remove("México")
print(paises)


#Ejemplo Crear un programa que solicite los email de los 
# alumnos de la UTD almacenar en una lista y posteriormente
#mostrar en pantalla los email sin duplicados.



listas_email=[]
RESP="si"

while RESP=="si":
   listas_email.append(input("Ingresa por favor tu Email escolar:"))
   RESP=input("Quieres ingresar otro Correo").lower()


listas_email_set=set(listas_email)
listas_email=list(listas_email_set)
print(listas_email)


  



