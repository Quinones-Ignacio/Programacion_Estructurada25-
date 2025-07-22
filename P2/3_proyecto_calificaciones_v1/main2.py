#proyecto 3 
# Crear un proyecto que permita Gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
# 2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como sus tres calificaciones
 

import calificaciones2

def main():
    datos = []  

    opcion=True
    while opcion:
     calificaciones2.borrarPantalla()
     opcion=calificaciones2.menu_principal()

     match opcion:
        case "1":  
            calificaciones2.agregar_calificaciones(datos)
            calificaciones2.esperarTecla()
        case "2":
            calificaciones2.mostrar_calificaciones(datos)
            calificaciones2.esperarTecla() 
        case "3":
            calificaciones2.calcular_promedios(datos)
            calificaciones2.esperarTecla()   
        case "4":
            opcion=False    
            calificaciones2.borrarPantalla()
            print("‼️ Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            calificaciones2.esperarTecla()
if __name__ == "__main__":
    main()