mes=""
importe=0
mesdedescuento='octubre'

mes=input("Introduce un mes (en minúsculas): ")
importe=int(input("Introduce tu importe del mes: "))

if(mes==mesdedescuento):
    print("¡15% en el mes de Octubre!")
    descuento = importe * 0.15
    importe-=descuento

print(f"El importe total es de: {importe}")