cantPalabras=0
diccionario={}
repeticiones=[]
palabras=[]
traduccion=[]

print("*****Bienvenido*****")
print("Diccionario de Español-Inglés")
cantPalabras=int(input("Introduce la cantidad de palabras que deseas agregar: "))

for x in range(cantPalabras):
    print("---------------------------------------")
    llave = input("Introduce tu palabra en español: ")
    if (llave in repeticiones):
        print("¡ERROR!")
        print("La palabra en español ya esta en el diccionario")
    else:
        repeticiones.append(llave)
        value = input("Introduce una asociación en inglés: ")
        diccionario[llave] = value
print("---------------------------------------")
frase=input("Introduce una frase en español: ")
palabras=frase.split()

for y in range(len(palabras)):
    palabra=palabras[y]
    if(palabra in repeticiones):
        print("ESTOY EN QUE LA PALABRA COINCICE")
        palabraIgual=diccionario.get(palabra)
        print("La palabra es ",palabraIgual)
        traduccion.insert(y, palabraIgual)
    else:
        print("ESTOY EN QUE LA PALABRA NO COINCICE :(")
        print("__________________")
        traduccion.insert(y,palabra)
        
fraseTraducida=" ".join(traduccion)
print(fraseTraducida)