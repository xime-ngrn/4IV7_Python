multiplicador=int(input("Da el multiplicador: "))
multiplicando=int(input("Da el multiplicando: "))
resultado=0

def multiplicar(x,y):
    if(x==0):
        global resultado
        resultado+=0
    else:
        #No usa recursividad :)
        for i in range(0,x):
            resultado+=y
    return resultado

multiplicar(multiplicador,multiplicando)
print(f"{multiplicador}*{multiplicando} es: {resultado}")