rango=range(0,20)
list(rango)
n=int(input("Introduce un numero: "))
contador=1

while n not in range(0,20):
    n=int(input("Introduce un numero: "))
    contador+=1
    continue

print(f"{n} está en el {rango}")
print("Numero de veces que se ingresó un número:",contador)