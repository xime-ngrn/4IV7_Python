from tkinter import  *

ventana3=Tk()
ventana3.title("Visualizar Palabra - Diccionario")
ventana3.geometry("467x350")
ventana3.resizable(0,0)

backgrnd= PhotoImage(file='letrasFondo.png')
fondo=Label(ventana3, image=backgrnd).place(x=0,y=0)

