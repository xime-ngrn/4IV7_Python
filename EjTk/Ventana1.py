from tkinter import *
ventana=Tk()
ventana2=Tk()
ventana.title("Ventana 1")
ventana.geometry("500x300")
ventana.config(bg="#B4E197")

etiqueta=Label(ventana, text="Hola mundo!",cursor="star")
etiqueta.pack(anchor="nw")
etiqueta.config(fg="#4E944F")
etiqueta2=Label(ventana, text="Segunda etiqueta",cursor="heart")
etiqueta2.pack(anchor="center")
etiqueta2.config(fg="#4E944F")
etiqueta3=Label(ventana,text="Ayoos mundo cruel!",cursor="pirate")
etiqueta3.pack(anchor="se")
etiqueta3.config(fg="#4E944F")

botoncito=Button(ventana, text="Botoncito", background="#E9EFC0", activebackground="#A2B38B", cursor="spraycan", command=ventana2.mainloop)
botoncito2=Button(ventana, text="Botoncito deshabilitado ;(", background="#78938A", activebackground="#C5D8A4", state="disabled")

botoncito2.pack()
botoncito.pack()

ventana.mainloop()