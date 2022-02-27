edad = 0
precio = 50
descuento = precio * 0.25

edad = int(input("Introduce tu edad: "))
if (edad < 10):
    precio -= descuento

print("Precio de acceso: ", precio)