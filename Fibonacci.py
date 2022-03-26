init=0
resultado=0
print("***** Serie de Fibonacci *****")
print("El primer número inicia en 0")
segundo=int(input("Introduce un número para la serie: "))
limite=int(input("Introduce un limite: "))

def fibonacci(n,m,limit):
    if limit != 0:
        limiteDentro=limit-1
        resultado=n+m
        print(resultado)
        fibonacci(resultado,n,limiteDentro)
    else:
        print("")


fibonacci(init,segundo,limite)
