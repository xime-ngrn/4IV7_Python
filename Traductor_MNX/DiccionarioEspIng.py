cantPalabras=0
diccionario={}
#llaves=[]
valores=[]

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for i in range(cantPalabras):
    llave=input("Introduce tu palabra en español: ")
    #pEspañol=input("Introduce tu palabra en español: ")
    #llaves.append(pEspañol)
    cantAsociaciones = int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    if(cantAsociaciones>1):
        for j in range(cantAsociaciones):
            global valores
            value = input("Introduce una asociación en inglés: ")
            valores.insert(j, value)
            print("||||| Terminó de agregar el valor, wiiii")
        diccionario[llave] = valores
    else:
        value = input("Introduce una asociación en inglés: ")
        diccionario[llave]=value

print("*******************")
print(diccionario)
print("*******************")
print(diccionario.keys())
print("********************")
print(diccionario.items())