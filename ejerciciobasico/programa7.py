print("Suma")
print("Introduce un número negativo para terminar")
acumulador=0
n = int(input("Introduce un número: "))

while n>0:
    acumulador += n
    n = int(input("Introduce un número: "))
    continue

if n<0:
    n=0
    acumulador += n

print(f"La suma final es {acumulador}")
