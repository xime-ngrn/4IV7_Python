rango=range(0,20)
list(rango)
n=int(input("Introduce un numero: "))

while n not in range(0,20):
    n=int(input("Introduce un numero: "))
    continue

print(f"{n} está en el {rango}")