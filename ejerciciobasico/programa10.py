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

horasExtra=int(input("Introduzca la cantidad de horas extra que trabajó: "))
for y in range(horasExtra):
    bonificacionHorasExtra = salarioBase * 0.5
    bon=bonificacionHorasExtra+salarioBase
    salarioHorasExtra+=bon

hijos=int(input("Introduzca la cantidad de hijos que tiene: "))
for x in range(hijos):
    b=salarioBase*0.5
    bonificacionHijos+=b

print("-----------------------------------------------------------------------")
horasNormal-=1
salarioFinal=bonificacionHijos+salarioHorasNormal+salarioHorasExtra
print(f"{nombre} tiene un salario total de ${salarioFinal}")
print(f" ☆Pago por {horasNormal} horas trabajadas ${salarioHorasNormal}")
print(f" ☆Pago por {horasExtra} horas trabajadas ${salarioHorasExtra}")
print(f" ☆Bonificación total por {hijos} hijos ${bonificacionHijos}")