calificaciones={}
promedio=0

print("★★★ Bienvenido ★★★")
cantidad=int(input("¿Cuántas calificaciones deseas ingresar? "))
print("Introduce tus calificaciones obtenidas en este parcial junto con cada materia.")
print(" ")
for i in range(cantidad):
    materia=input("Introduce el nombre de la materia: ")
    if(materia in calificaciones):
        print("La materia ya contiene una calificación")
    else:
        calif = int(input("Introduce tu calificación obtenida: "))
        promedio+=calif
        calificaciones[materia] = calif


promedio/=cantidad

if(promedio<6):
    print("-------------------------------")
    print("¡Hay que esforzarse el doble!")
    print("Tu promedio es de {:.3f}".format(promedio))
elif(promedio<8.5):
    print("-------------------------------")
    print("¡Buen esfuerzo!")
    print("Tu promedio es de {:.3f}".format(promedio))
else:
    print("-------------------------------")
    print("¡Felicidades!")
    print("Tu promedio es de {:.3f}".format(promedio))

print("-------------------------------")
for i in calificaciones:
    print("{0} en {1}".format(calificaciones.get(i), i))
