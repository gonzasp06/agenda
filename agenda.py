def cargar_agenda():
    try:
        with open('agenda.txt', 'r') as archivo:
            contactos = archivo.readlines()
            agenda = [contacto.strip() for contacto in contactos]
    except FileNotFoundError:
        agenda = []
    return agenda

def guardar_agenda(agenda):
    with open('agenda.txt', 'w') as archivo:
        for contacto in agenda:
            archivo.write(contacto + '\n')

def mostrar_contactos(agenda):
    if not agenda:
        print("Agenda vacia compa")
    else: 
        print(" \n ")
        print("-----Tus contactos guardados son: -----")
        for contacto in agenda:
            print(contacto)

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    contacto = f"{nombre}: {telefono}"
    agenda.append(contacto)
    guardar_agenda(agenda)
    print("El contacto ha sido guardado crack.")

def menu():
    agenda = cargar_agenda()
    while True:
        print("\n------ Agenda Telefónica ------")
        print("1. Mostrar contactos")
        print("2. Agregar contacto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_contactos(agenda)
        elif opcion == "2":
            agregar_contacto(agenda)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

menu()  