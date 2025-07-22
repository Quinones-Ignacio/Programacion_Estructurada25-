#agenda_contactos = {
#                   "RUBEN": ["6181234535", "ruben@gmail.com"],
#                   "DANIEL": ["6182110278", "daniel@gmail.com"],
#                   "XIMENA": ["6183910678", "ximena@gmail.com"], 
#}


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
    input("✅Oprima cualquier tecla para continuar")  

def menu_principal():
  print("📒.:: Sistema de Gestión de Agenda de Contactos ::..📒 \n 1️⃣-  Agregar contacto  \n 2️⃣-  Mostrar todo los Contactos \n 3️⃣- Buscar contacto por nombre \n 4️⃣- Modificar Contacto " \
  "\n 5️⃣- Eliminar contacto \n 6️⃣- Salir del sistema")
  opcion=input("👉 Elige una opción ( 1️⃣ - 6️⃣ ): ") 
  return opcion 

def agregar_contacto(agenda):
    borrarPantalla()
    print("👤 Agregar Contactos")
    nombre = input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("❌ El contacto ya existe. Intenta con otro nombre.")
    else:
       tel = input("Teléfono del contacto: ").strip()
       email = input("Email del contacto: ").upper().strip()
       agenda[nombre] = [tel, email]
       print("✅ Contacto agregado con éxito")
   
def mostrar_contacto(agenda): 
    borrarPantalla()
    print("👤 Mostrar Contactos")
    if not agenda:
        print("❌ No hay contactos para mostrar.")
    else:
        print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
        print(f"-" *60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15} {datos[1]:<15}")
            print(f"-" *60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("👤 Buscar Contactos")
    if not agenda:
        print("❌ No hay contactos para buscar.")
    else:
        nombre=input("Ingrese el nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print(f"-" *60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print(f"-" *60)
        else:
            print(f"❌ No existe el contacto ")
        
def modificar_contacto(agenda):
    borrarPantalla()
    print("👤 Modificar Contactos")
    if not agenda:
        print("❌ No hay contactos para modificar.")
    else:
        nombre = input("📝 Ingrese el nombre del contacto: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print(f"-" *60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print(f"-" *60)
            resp = input("🤔 ¿Desea modificar este contacto? (si/no): ").lower().strip()
            if resp=="si":
               tel = input("Ingrese el teléfono: ").strip()
               email = input("Ingrese el email: ").upper().strip()
               agenda[nombre] = [tel, email]
               print("✅ Contacto modificado con éxito")
        else:
            print(f"❌ No existe el contacto")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("👤 Eliminar Contactos")
    if not agenda:
        print("❌ No hay contactos para eliminar.")
    else:
        nombre=input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print(f"-" *60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print(f"-" *60)
            resp = input("🤔 ¿Desea eliminar este contacto? (Si/No): ").lower().strip()
            if resp=="si":
                agenda.pop(nombre)
                print("✅ Contacto eliminado con éxito")
        else:
            print(f"❌ No existe el contacto")
