cantPalabras=0
diccionario={}
valores=[]
valores1=[]
valores2=[]
valores3=[]
asociacionesMultiples=0

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for i in range(cantPalabras):
    print("---------------------------------------")
    llave=input("Introduce tu palabra en español: ")
    cantAsociaciones = int(input("Introduce la cantidad de palabras en inglés deseadas: "))

    if (cantAsociaciones > 1):
        if(asociacionesMultiples==0):
            for j in range(cantAsociaciones):
                value = input("Introduce una asociación en inglés: ")
                valores.insert(j, value)
            diccionario[llave] = valores
            asociacionesMultiples += 1
            break
        if(asociacionesMultiples==1):
            for j in range(cantAsociaciones):
                value = input("Introduce una asociación en inglés: ")
                valores1.insert(j, value)
            diccionario[llave] = valores1
            asociacionesMultiples += 1
            break
        if(asociacionesMultiples==2):
            for j in range(cantAsociaciones):
                value = input("Introduce una asociación en inglés: ")
                valores2.insert(j, value)
            diccionario[llave] = valores2
            asociacionesMultiples += 1
            break
        if (asociacionesMultiples == 3):
            for j in range(cantAsociaciones):
                value = input("Introduce una asociación en inglés: ")
                valores3.insert(j, value)
            diccionario[llave] = valores3
            asociacionesMultiples += 1
            break
    else:
        value = input("Introduce una asociación en inglés: ")
        diccionario[llave] = value

print("*******************")
print(diccionario)
print("*******************")
print(diccionario.keys())
print("********************")