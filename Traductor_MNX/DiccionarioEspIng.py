cantPalabras=0
diccionario={}
llaves=[]
valores=[]

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for i in range(cantPalabras):
    pEspañol=input("Introduce tu palabra en español: ")
    llaves.insert(pEspañol)
    cantAsociaciones = int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    if(cantAsociaciones>1):
        for j in range(cantAsociaciones):
            value = input("Introduce una asociación en inglés: ")
            valores.insert(j, value)
        diccionario[llaves] = valores
        #no guarda nada en el diccionario
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