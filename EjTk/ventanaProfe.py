import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.etiqueta_temp_celsius = ttk.Label(
        parent, text="Temperatura en ºC:")
        self.etiqueta_temp_celsius.place(x=20, y=20)

ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)

app = Aplicacion(ventana)
ventana.mainloop()