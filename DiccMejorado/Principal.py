# interfaz inicio
# archivos para guardar palabras, modificar y visualizar
# poo para crear archivos y realizar todo eso :)
# ¡¿CÓMO VOY A FILTRAR?! Ni idea :)


from tkinter import *

import AgregarPalabra

ventana=Tk()
ventana.title("Principal - Diccionario")
ventana.geometry("467x350")
ventana.resizable(0,0)

bg=PhotoImage(file='letrasfondo.png')
fondo=Label(ventana, image=bg)
fondo.place(x=0,y=0)

label=Label(ventana, text="Diccionario Español-Inglés", font=("Garamo3nd",28), bg="#DAE5D0")

agregarPalabra=Button(ventana, text="Agregar Palabra", bg="#C4DDFF", fg="#383838", font=("Gotham", 18), relief=RIDGE)
visualizarPalabras=Button(ventana, text="Visualizar Palabras", bg="#99C4C8", fg="#383838", font=("Gotham", 18))
modificarTraduccion=Button(ventana, text="Modificar la Traducción de una Palabra", bg="#68A7AD", fg="#383838", font=("Gotham", 18))


label.pack()
agregarPalabra.place(x=120, y=80)
visualizarPalabras.place(x=110, y=160)
modificarTraduccion.place(x=10, y=240)
ventana.mainloop()