from random import randint

intento=10
oportunidades=True
palabraf=""
posicion=0

animales=("gato", "pato", "oso", "leon", "huron", "leon", "murcielago", "raton", "oveja", "vibora", "zebra", "sapo")

def generarNumero():
    numero = randint(0, 11)
    return numero


def letraCorrecta(palabra, letra, palabraf):
    print("*")
    posicion=palabra.find(letra)
    palabraf = palabraf[:posicion] + letra + palabraf[posicion + 1:]
    return palabraf

p=generarNumero()
palabrae=animales[p]
letras=set(palabrae)

print("★★★ Bienvenido ★★★")
print("Ahorcado, adivina al animal")
print("Tienes 10 intentos para adivinar la palabra, ¡Buena suerte!")
for i in palabrae:
        palabraf += "_"
print(palabraf)
print("")
while oportunidades:
        if (intento!=0):
                print(" ")
                letra=input("Letra: ")
                print("- Intentos: ",intento)
                if(letra in letras):
                        palabraf=letraCorrecta(palabrae, letra, palabraf)
                        print(palabraf)
                        if(palabraf==palabrae):
                                print("¡Felicidades!")
                                break
                else:
                        print("La letra no está en la palabra")
                intento-=1
                oportunidades = True
        else:
                print("¡Buen intento!")
                oportunidades = False

print("★★★★★★★★★★★★★★★★★★")
print("La palabra es ",palabrae)
print("Juego terminado")