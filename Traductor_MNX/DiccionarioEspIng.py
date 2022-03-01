cantPalabras=0
diccionario={}
llaves=[]
valores=("vacio","vacio1")

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for i in range(cantPalabras):
    pEspañol=input("Introduce tu palabra en español: ")
    llaves.insert(pEspañol)
    global llaves
    cantAsociaciones = int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    if(cantAsociaciones>1):
        for j in range(cantAsociaciones):
            val = list(valores)
            value = input("Introduce una asociación en inglés: ")
            val[j] = value
            global val
        valores = tuple(val)
        diccionario[llaves] = valores
    else:
        value = input("Introduce una asociación en inglés: ")
        diccionario[llaves]=value

print("*******************")
print("*******************")
print(diccionario)
print("*******************")
print(diccionario.keys())
print("********************")
print(diccionario.items())