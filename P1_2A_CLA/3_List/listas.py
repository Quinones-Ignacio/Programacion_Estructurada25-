import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
os.system("clear")
numeros=[5,10.15,20]
#1er forma
print(numeros)

#2da froma

for i in numeros:
    print(i)

#3er forma trabaja con los indices

for i in range(0,len(numeros)):
    print(numeros[i]) 

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la 
#coincidencia de una palabra

os.system("clear")

palabras=["Hola","Adios","Bienvenido","Gracias"]
palabra_buscar=input("Dame la palabra a buscar")

palabras["","",""]

palabras[0]="Hola"
palabras[1]="Adios"
palabras[2]="Bienvenido"

print(palabras)

#1er forma
palabras=["Hola","Adios","Bienvenido","Gracias"]
palabra_buscar=input("Dame la palabra a buscar")
if palabra_buscar in palabras:
   print("Se encontro la palabra")
else:
    print("No encontro la palabra")

#2da forma
encontro=False
for i in palabra_buscar: 
    if i==palabra_buscar:
        encontro=True
    
    if encontro:
        print("Se encontro la palabra")
    else:
        print("No se encontro la palabra")

#3ra Forma
encontro=False
for i in range(0,len(numeros)):
    if palabras[i]==palabra_buscar:
        encontro=True
    
    if encontro:
        print("Se encontro la palabra")
    else:
        print("No se encontro la palabra")

#Ejemplo 3 Añadir elementos a la lista
numeros=[]
opc="si"

while opc=="si":
     numeros.append(float(input("Dame un numero entero o decimal")))
     opc=input("¿Deseas solicitar otro numero" ("si/no")).lower()

print(numeros) 


#Ejemplo 4 Crear una lista multidimensional (matriz) que
#almacene el nombre y telefono de 4 personas

agenda=[
      ["Carlos","6182120271"],
      ["Juan","6181234567"],
      ["Pedro","6182690012"],
]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 
