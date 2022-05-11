import POO
from POO import *
bandera=True
figura1=Figura1Parametro()
figura2=Figura2Parametros()

print("★★★ Bienvenido ★★★")
while(bandera==True):
    print(" Figuras ")
    print("1. Circulo")
    print("2. Triángulo")
    print("3. Cuadrado")
    print("4. Rectángulo")
    print("5. Terminar")
    opcion=int(input("Selecciona una figura: "))
    print(" ")

    if(opcion==1):
        r=float(input("Introduce el radio: "))
        area=figura1.areaCirculo(r)
        per=figura1.perimetroCirculo(r)
        print("El área del círculo es {:.3f} y su perímetro {:.3f}".format(area, per))
        print(" ")
    elif(opcion==2):
        base=float(input("Introduce la base: "))
        alt=float(input("Introduce la altura: "))
        area=figura2.areaTriangulo(base, alt)
        per=figura1.perimetroTriangulo(base)
        print("El área del triángulo es {:.3f} y su perímetro {:.3f}".format(area, per))
        print(" ")
    elif(opcion==3):
        lado = float(input("Introduce el lado: "))
        area = figura1.areaCuadrado(lado)
        per = figura1.perimetroCuadrado(lado)
        print("El área del cuadrado es {:.3f} y su perímetro {:.3f}".format(area, per))
        print(" ")
    elif(opcion==4):
        base = float(input("Introduce la base: "))
        alt = float(input("Introduce la altura: "))
        area = figura2.areaRectangulo(base, alt)
        per = figura2.perimetroRectangulo(base, alt)
        print("El área del rectángulo es {:.3f} y su perímetro {:.3f}".format(area, per))
        print(" ")
    elif(opcion==5):
        print("--- Finalizar")
        bandera=False
    else:
        print("--- La opción no es válida")
