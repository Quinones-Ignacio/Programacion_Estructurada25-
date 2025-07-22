
#dic u objeto para almacena los atributos (nombre, categoria, clasificarcion, genero, idioma)

#peliculas={
#           "nombre":"",
#            "categoria":"",
#            "clasificacion":"",
#           "genero":"",
#           "idioma":""
#}
pelicula={}

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    print("\n\t\tOprima cualquier tecla para continuar...")
    input() 

def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::.\n")
    #pelicula["nombre"]=input("Ingressa el nombre: ").upper().strip()
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPeliculas():
   borrarPantalla()
   print("\n\t.:: Consultar o mostrar la Pelicula ::.\n ")
   if len(pelicula)>0:
      for i in pelicula:
         print(f"\t {(i)} : {pelicula[i]}")
      else:
       print("\t.:: No hay peliculas en el sistema ::.")

def borrarPeliculas():
     borrarPantalla()
     print("\n\t.:: Borrar o quitar todas las Peliculas ::. \n")
     resp=input("Deseas borrar o quitar todas las peliculas del sitema? (Si/No)")
     if resp =="si":
         pelicula.clear()
         print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def agregarCaracteristicaPeliculas():
     borrarPantalla()
     print("\n\t.:: Agregar caracteristicas a peliculas ::. \n")
     atributo=input("Ingresa la nueva caracteriztica de la pelicula: ").lower().strip()
     valor=input("Ingresa el valor de la caracteriztica de la pelicula: ").lower().strip()
     # pelicula.update({atributo:valor})
     pelicula[atributo]=valor
     print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def modificarCaracteristicaPeliculas():
   borrarPantalla()
   print("\n\t.:: Modificar Características a Películas  ::. \n")
   if len(pelicula)>0:
    print(f"\n\tValor actuales: \n ")
    for i in pelicula:
      print(f"\t {(i)} : {pelicula[i]}")
      resp=input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
      if resp=="si":
        pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
   else:
     print("\t..:: No hay peliculas en Sistema  ::..")
     esperarTecla()

def borrarCaracteristicaPeliculas():
    print("\n\t.:: Borrar una Característica de la Película ::.\n")
    
    for clave, valor in pelicula.items():
        print(f"{clave} : {valor}")
    
    