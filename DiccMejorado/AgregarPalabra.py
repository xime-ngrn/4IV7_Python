from tkinter import *

ventana1=Toplevel()
ventana1.title("Agregar Palabra - Diccionario")
ventana1.geometry("467x350")
ventana1.resizable(0,0)

backg= PhotoImage(file='letrasFondorRen.png.png')
fondo=Label(ventana1, image=backg).place(x=0,y=0)

label=Label(ventana1, text="Agregar Palabra", font=("Garamond",28), bg="#C4DDFF")

labelEsp=Label(ventana1, text="Español", font=("Gotham", 16), bg="#EEE4AB")
español=Entry(ventana1, bg="#FEFBE7", fg="#383838", font=("Bickham script pro", 16), insertbackground="#68A7AD")
labelIng=Label(ventana1, text="Inglés", font=("Gotham", 16), bg="#EEE4AB")
ingles=Entry(ventana1, bg="#FEFBE7", fg="#383838", font=("Bickham script pro", 16), insertbackground="#68A7AD")
agregar=Button(ventana1, text="Agregar Palabra", font=("Bickham script pro", 15), bg="#C4DDFF", fg="#383838", pady=10, padx=10)


label.pack()
labelEsp.place(x=10, y=80)
español.place(x=120, y=80)
labelIng.place(x=20, y=150)
ingles.place(x=120, y=150)
agregar.place(x=145, y=250)