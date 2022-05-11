from tkinter import Button, Entry, Tk, Label, StringVar

def sumar():
    x=numero1.get()
    y=numero2.get()
    resultado=x+y
    print(resultado)

ventana=Tk()
label=Label(ventana, text="Introduce 2 números para una suma")

numero1=Entry(ventana)
numero2=Entry(ventana)

boton=Button(ventana, text="Sumar :I", command=sumar)

numero1.pack()
numero2.pack()
boton.pack()

ventana.mainloop()