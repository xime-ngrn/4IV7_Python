sueldo=0
aumento=0

sueldo=int(input("Introduce tu sueldo: "))
if(sueldo<4000):
    aumento=sueldo*0.15
    sueldo+=aumento
    print("Aumento del 15%")
else:
    aumento=sueldo*0.08
    sueldo+=aumento
    print("Aumento del 8%")

print(f"El sueldo final es de {sueldo}")