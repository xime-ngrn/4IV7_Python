bonificacionHijos=0
salarioHorasNormal=0
salarioHorasExtra=0
salarioFinal=0

print("Bienvenido")

nombre=input("Introduzca su nombre: ")
salarioBase=float(input("Introduzca su salario al trabajar una hora normal: "))
horasNormal=int(input("Introduzca la cantidad de horas que trabajó: "))
horasNormal+=1
for x in range(horasNormal):
    salarioHorasNormal=salarioBase*x
print(f"por trabajar {horasNormal} horas tu pago es {salarioHorasNormal}")

print("-----------------------------------------------------------------------")

horasExtra=int(input("Introduzca la cantidad de horas extra que trabajó: "))
for y in range(horasExtra):
    bonificacionHorasExtra = salarioBase * 0.5
    bon=bonificacionHorasExtra+salarioBase
    salarioHorasExtra+=bon

print(f"La bonificación de 1 hora extra es de {bonificacionHorasExtra}")
print(f"Por trabajar {horasExtra} tu pago es {salarioHorasExtra}")

print("-----------------------------------------------------------------------")

hijos=int(input("Introduzca la cantidad de hijos que tiene: "))
for x in range(hijos):
    b=salarioBase*0.5
    bonificacionHijos+=b
    print(f"La bonificacion del 50% por sus {hijos} es de {bonificacionHijos}")

print("-----------------------------------------------------------------------")

salarioFinal=bonificacionHijos+salarioHorasNormal+salarioHorasExtra
print(f"El salario final es de {salarioFinal}")
