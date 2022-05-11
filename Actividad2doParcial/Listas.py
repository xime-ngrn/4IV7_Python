print("★★★★★ Lista de Invitados para una Fiesta ★★★★★")
invitados=[]
bandera=True

while(bandera):
    print(" ")
    print("1. Agregar invitado")
    print("2. Ver lista de invitados")
    print("3. Eliminar invitado")
    print("4. Eliminar a todos los invitados")
    print("5. Terminar")
    print(" ")
    opcion = int(input("Introduce la opción que deseas: "))
    if (opcion == 1):
        invitado=input("Nombre del invitado: ")
        invitados.append(invitado)
    elif (opcion == 2):
        for i in range(0, len(invitados)):
            nom = invitados[i]
            print(f"{i + 1}. {nom}")
    elif (opcion == 3):
        forma=input("¿Deseas eliminar al invitado por su nombre? ")
        if(forma=="Si" or forma=="si"):
            eliminar = input("Introduce el nombre del invitado a eliminar: ")
            invitados.remove(eliminar)
        else:
            eliminar=int(input("Introduce el índice en la lista del inivitado al que deseas eliminar: "))
            eliminar-=1
            invitados.pop(eliminar)
        print("El invitado ha sido eliminado")
    elif (opcion == 4):
        invitados.clear()
        print("La lista está vacía")
    elif (opcion == 5):
        print("***** Lista terminada *****")
        print("Total de invitados: ",len(invitados))
        for i in range(0, len(invitados)):
            nom = invitados[i]
            print(f"★ {nom}")
        bandera=False
    else:
        print("La opción no es válida")
