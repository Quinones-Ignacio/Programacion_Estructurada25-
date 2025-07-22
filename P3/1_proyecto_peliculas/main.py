
#Proyecto 1.
#crear un proyecto que permita gestionar (administrar peliculas), 
# colocar un menu de opciones para agregar, borrar, modificar, consultar, buscar peluculas
# Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2._ Utilizar dic para almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma) de las peliculas
#3. - Utilizar e implementar una BD relacional en MySQL
import peliculas

opcion=True
while opcion:
    print("\n\t\t\t..🎬::: CINEPOLIS CLON :::... \n\t\t..🍿::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear 🆕 \n\t\t 2.- Borrar 🗑️ \n\t\t 3.- Mostrar 📋 \n\t\t 4.- Buscar 🔍 \n\t\t 5.- Modificar ✏️ \n\t\t 6.- SALIR 🚪")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
             
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()    
        case "4":
            peliculas.buscarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        
        case "6":
            opcion=False    
            peliculas.borrarPantalla()
            print("\n\t🚪 Terminaste la ejecución del SW. ¡Hasta pronto! 👋😊")
        case _: 
            opcion
            input("\n\t❌ Opción inválida, vuelva a intentarlo... por favor 🙏")

      


      




    

