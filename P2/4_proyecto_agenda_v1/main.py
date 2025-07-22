#


import agenda

def main():
    mi_agenda={}   

    opcion=True
    while opcion:
     agenda.borrarPantalla()
     opcion=agenda.menu_principal()

     match opcion:
        case "1":  
            agenda.agregar_contacto(mi_agenda)
            agenda.esperarTecla()
        case "2":
            agenda.mostrar_contacto(mi_agenda)
            agenda.esperarTecla() 
        case "3":
            agenda.buscar_contacto(mi_agenda)
            agenda.esperarTecla() 
        case "4":
            agenda.modificar_contacto(mi_agenda)
            agenda.esperarTecla()  
        case "5":
            agenda.eliminar_contacto(mi_agenda)
            agenda.esperarTecla()
        case "6":
            opcion=False    
            agenda.borrarPantalla()
            print("‼️ Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperarTecla()
if __name__ == "__main__":
    main()