cantPalabras=0
diccionario={}
#llaves=[]
valores=()

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for i in range(cantPalabras):
    llave=input("Introduce tu palabra en español: ")
    #pEspañol=input("Introduce tu palabra en español: ")
    #llaves.append(pEspañol)
    cantAsociaciones = int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    if(cantAsociaciones>1):
        #mala idea usar tuplas, no funcionan de igual forma
        #IDEAAAAAAAA
        #Crear listas infinitas como dios me de a entender
        for j in range(cantAsociaciones):
            val = list(valores)
            value = input("Introduce una asociación en inglés: ")
            val.insert(j,value)
        valores = tuple(val)
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