class Archivo():
    def __init__(self):
        self.nombreArch="diccionario.txt"
        self.ruta="elementos/diccionario.txt"
        self.fichero=None
        self.español=""
        self.ingles=""

    def crearFichero(self):
        with open (self.ruta, "w", encoding="UTF-8") as self.fichero:
            print("*** Se ha creado el fichero ***")
            print(f"Posición actual: {self.fichero.tell()}")

    def cerrarFichero(self):
        self.fichero.close()

    def escribirFichero(self, español, ingles):
        with open(self.ruta, "a+", encoding="UTF-8") as self.fichero:
            print("*** Escribir en el fichero ***")
            print(f"Posición actual: {self.fichero.tell()}")
            self.español = español
            self.ingles = ingles

            palabras = f"{self.español}-{self.ingles}\n"
            print(palabras)
            self.fichero.write(palabras)
            print("*** Se ha escrito en el fichero ***")
            print(f"Posición actual: {self.fichero.tell()}")
