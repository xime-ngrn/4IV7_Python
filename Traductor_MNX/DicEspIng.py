cantPalabras=0
diccionario={}
palabrasIngles=[]

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
#BUCLE WHILE PARA REPETIR LA INTRODUCCION DE PALABRAS

cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))
for i in range(cantPalabras):
    key=input("Introduce una palabra en español: ")
    cantAsociaciones=int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    for j in range(cantAsociaciones):
        value=input("Introduce una palabra asociada: ")
        diccionario[key] = value
        #solo guarda un valor
        #si utilizo una lista, todas las llaves tienen todos los valores de la lista

    print("-----------")
    print(diccionario)
    print("-----------")
    print(diccionario.keys())