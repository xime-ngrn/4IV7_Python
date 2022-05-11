from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.geometry("460x500")
ventana.title("Bloc de Notas - Personalizado")

#Función para creador y borrar
def mostrarCreador():
    messagebox.showinfo(title="Creador", message="Creado por Ximena Moreno Noguerón del grupo 4IV7")

def borrar():
    texto.delete("1.0","end")

#Funciones para los temas
def interfazClara():
    archivo.config(activebackground="#FFFBE7", activeforeground="#383838", bg="#DDDDDD", fg="#383838")
    personalizar.config(activebackground="#FFFBE7", activeforeground="#383838", bg="#DDDDDD", fg="#383838")
    texto.config(bg="#ECECEC", fg="#383838")

def interfazObscura():
    archivo.config(activebackground="#E6DDC4", activeforeground="#000000", bg="#000000", fg="#EADEDE")
    personalizar.config(activebackground="#E6DDC4", activeforeground="#000000", bg="#000000", fg="#EADEDE")
    texto.config(bg="#2C272E", fg="#EADEDE")

def interfazVerde():
    archivo.config(bg="#92BA92", activebackground="#B4E197", activeforeground="#019267", fg="#383838")
    personalizar.config(bg="#92BA92", activebackground="#B4E197", activeforeground="#019267", fg="#383838")
    texto.config(bg="#C3E5AE", fg="#383838")

def interfazMorada():
    archivo.config(bg="#E4AEC5", activebackground="#85586F", activeforeground="#D18CE0", fg="#000000")
    personalizar.config(bg="#E4AEC5", activebackground="#85586F", activeforeground="#D18CE0", fg="#000000")
    texto.config(bg="#a18594", fg="#000000")

def interfazAzul():
    archivo.config(bg="#B7CADB", activebackground="#678983", activeforeground="#000000", fg="#383838")
    personalizar.config(bg="#B7CADB", activebackground="#678983", activeforeground="#000000", fg="#383838")
    texto.config(bg="#89B5AF", fg="#181D31")


texto=Text(ventana, width="450", height="490")
barramenu=Menu(ventana)
archivo=Menu(barramenu)
archivo.add_command(label="Creador", command=mostrarCreador)
archivo.add_command(label="Guardar", state="disabled")
archivo.add_command(label="Borrar todo", command=borrar)
archivo.add_command(label="Compartir", state="disabled")
archivo.add_command(label="Salir", command=ventana.quit)

personalizar=Menu(barramenu)
personalizar.add_command(label="Claro", command=interfazClara)
personalizar.add_command(label="Obscuro", command=interfazObscura)
personalizar.add_command(label="Verde", command=interfazVerde)
personalizar.add_command(label="Lila", command=interfazMorada)
personalizar.add_command(label="Azul", command=interfazAzul)

barramenu.add_cascade(label="Archivo", menu=archivo)
barramenu.add_cascade(label="Temas", menu=personalizar)

interfazClara()
ventana.config(menu=barramenu)
texto.pack()
ventana.mainloop()
