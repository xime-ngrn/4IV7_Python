from elementos import *
from Archivos import Archivo
from tkinter import *

fichero=Archivo()

class Ventana():
    def __init__(self):
        self.nombre = ""
        self.fondo="elementos/letrasfondo.png"
        self.labelFondo=None
        self.__palabraEspañol=""
        self.__palabraIngles=""
        self.__diccionario={}
        self.__palabrasEsp=self.__diccionario.keys()
        self.__palabrasIng=self.__diccionario.values()
        fichero.crearFichero()

    def principal(self):
        self.nombre="Principal - Diccionario"

        self.ventanaP = Tk()
        self.ventanaP.title(self.nombre)
        self.ventanaP.geometry("467x350")
        self.ventanaP.resizable(0, 0)
        bg = PhotoImage(file=self.fondo)
        self.labelFondo=Label(self.ventanaP, image=bg)
        labelTitulo=Label(self.ventanaP, text="Diccionario Español-Inglés", font=("Garamond",28), bg="#DAE5D0")

        agregarPalabra = Button(self.ventanaP, text="Agregar Palabra", bg="#C4DDFF", fg="#383838", font=("Gotham", 18),
                                highlightcolor="#557B83", relief=RIDGE, command=self.agregarP)
        visualizarPalabras = Button(self.ventanaP, text="Visualizar Palabras", bg="#99C4C8", fg="#383838",
                                    highlightcolor="#557B83", font=("Gotham", 18), relief=RIDGE, command=self.irPrincipalVisualizar)
        modificarTraduccion = Button(self.ventanaP, text="Modificar la Traducción de una Palabra", bg="#68A7AD", fg="#383838",
                                     highlightcolor="#557B83", font=("Gotham", 18), relief=RIDGE, command=self.modificarP)
        Traduccion = Button(self.ventanaP, text="Traducir una Frase", bg="#97C4B8", fg="#383838", highlightcolor="#557B83",
                            font=("Gotham", 18), relief=RIDGE, command=self.irTraducir)

        self.labelFondo.place(x=0, y=0)
        labelTitulo.place(x=40, y=10)
        agregarPalabra.place(x=130, y=80)
        visualizarPalabras.place(x=115, y=160)
        modificarTraduccion.place(x=10, y=240)
        Traduccion.place(x=100, y=300)
        self.ventanaP.mainloop()


    def agregarP(self):
        self.nombre = "Agregar Palabras - Diccionario"
        self.ventanaP.destroy()

        def agregarValores():
            español=pespañol.get().lower()
            ingles=pingles.get().lower()
            labelValores=f" Palabras Obtenidas: {español}-{ingles}"
            labelP.config(text=labelValores)
            self.agregarPFichero(español, ingles)
            self.__diccionario[español]=ingles
            print("----- Agregar Palabras -----")
            print("Las palabras agregadas fueron {0}-{1}".format(español, ingles))
            print(self.__diccionario)

        self.ventanaAgregarP=Tk()
        self.ventanaAgregarP.title(self.nombre)
        self.ventanaAgregarP.geometry("467x350")
        self.ventanaAgregarP.resizable(0, 0)
        self.labelFondo = Label(self.ventanaAgregarP, bg="#C4DDFF", padx=467, pady=350)

        label = Label(self.ventanaAgregarP, text="Agregar Palabra", font=("Garamond", 28), bg="#C4DDFF")

        labelEsp = Label(self.ventanaAgregarP, text=" Español ", font=("Gotham", 16), bg="#E5EFC1")
        pespañol = Entry(self.ventanaAgregarP, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16), )

        labelIng = Label(self.ventanaAgregarP, text=" Inglés ", font=("Gotham", 16), bg="#E5EFC1")
        pingles = Entry(self.ventanaAgregarP, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))

        labelP=Label(self.ventanaAgregarP, text=" Palabras Obtenidas: ", font=("Gotham", 16), bg="#E5EFC1")

        agregar = Button(self.ventanaAgregarP, text="Agregar Palabra", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                         pady=10, padx=10, relief=RIDGE, command=agregarValores)
        regresar=Button(self.ventanaAgregarP, text="Regresar a Principal", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                         pady=10, padx=10, relief=RIDGE, command=self.regresarPrincipalAgregar)


        label.place(x=120, y=10)
        labelEsp.place(x=10, y=80)
        pespañol.place(x=120, y=80)
        labelIng.place(x=20, y=150)
        pingles.place(x=120, y=150)
        labelP.place(x=100, y=200)
        self.labelFondo.place(x=0, y=0)
        agregar.place(x=250, y=250)
        regresar.place(x=30, y=250)
        self.ventanaAgregarP.mainloop()


    def visualizarP(self):
        self.nombre="Visualizar Palabras - Diccionario"

        self.ventanaVisualizarP = Tk()
        self.ventanaVisualizarP.title(self.nombre)
        self.ventanaVisualizarP.geometry("467x550")
        self.labelFondo = Label(self.ventanaVisualizarP, bg="#99C4C8", padx=467, pady=350)

        label = Label(self.ventanaVisualizarP, text="Visualizar Palabras", font=("Garamond", 28), bg="#99C4C8")

        palabras=Frame(self.ventanaVisualizarP, padx=10, pady=10)
        for i in self.__diccionario:
            esp=i
            ing=self.__diccionario.get(i)
            espIng=f"{esp}-{ing}\n"
            p=Label(palabras, text=espIng, font=("Gotham", 16), bg="#E5EFC1")
            p.pack()

        buscarSin=Button(self.ventanaVisualizarP, text="Buscar palabra", font=("Constantia", 15), bg="#C5D8A4", fg="#383838",
                      pady=10, padx=10, relief=RIDGE,command=self.irPalabrasSinonimo)
        buscarLetra=Button(self.ventanaVisualizarP, text="Buscar por letra", font=("Constantia", 15), bg="#B4E197", fg="#383838",
                      pady=10, padx=10, relief=RIDGE,command=self.irPalabrasLetra)
        regresar = Button(self.ventanaVisualizarP, text="Regresar a Principal", font=("Constantia", 15), bg="#E5EFC1",
                          fg="#383838", pady=10, padx=10, relief=RIDGE, command=self.regresarPrincipalVisualizar)

        label.place(x=100, y=10)
        self.labelFondo.place(x=0, y=0)
        regresar.place(x=130, y=130)
        buscarSin.place(x=35, y=60)
        buscarLetra.place(x=245, y=60)
        palabras.place(x=5, y=200)

        self.ventanaVisualizarP.mainloop()


    def buscarPalabrasSinonimo(self):
        self.nombre="Buscar Palabras (Sinónimo) - Diccionario"

        def buscarPalabra():
            p=palabra.get()
            pal = Label(self.ventanaBuscarSin, text="", font=("Gotham", 16), bg="#E5EFC1")
            for i in self.__palabrasEsp:
                error.config(text="")
                if(i==p):
                    #la palabra sí esta
                    esp = i
                    ing = self.__diccionario.get(i)
                    espIng = f"{esp}-{ing}\n"
                    pal.config(text=espIng)
                    pal.place(x=10, y=230)
                else:
                    error.config(text="La palabra no se ha encontrado")
            print("----- Se ha buscado la palabra -----")

        self.ventanaBuscarSin=Tk()
        self.ventanaBuscarSin.title(self.nombre)
        self.ventanaBuscarSin.geometry("490x370")
        self.ventanaBuscarSin.resizable(0, 0)
        self.labelFondo = Label(self.ventanaBuscarSin, bg="#C5D8A4", padx=467, pady=350)
        label = Label(self.ventanaBuscarSin, text="Buscar Palabras Por Sinónimos", font=("Garamond", 28), bg="#99C4C8")

        label2 = Label(self.ventanaBuscarSin, text="Palabra: ", font=("Gotham", 16), bg="#E5EFC1")
        palabra = Entry(self.ventanaBuscarSin, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))
        buscar = Button(self.ventanaBuscarSin, text="Buscar", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                        pady=10, padx=10, relief=RIDGE, command=buscarPalabra)
        error = Label(self.ventanaBuscarSin, text="", font=("Gotham", 16), bg="#E5EFC1", fg="#F32424")

        regresar = Button(self.ventanaBuscarSin, text="Regresar a Visualizar Palabras", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                         pady=10, padx=10, relief=RIDGE, command=self.regresarPalSin)


        label.place(x=15, y=10)
        label2.place(x=10, y=150)
        palabra.place(x=120, y=150)
        buscar.place(x=370, y=140)
        error.place(x=10, y=185)
        self.labelFondo.place(x=0, y=0)
        regresar.place(x=10, y=70)
        self.ventanaBuscarSin.mainloop()


    def buscarPalabrasLetra(self):
        self.nombre = "Buscar Palabras (Letra) - Diccionario"

        def buscarLetra():
            l=letra.get()
            p = Label(palabras, text="", font=("Gotham", 16), bg="#E5EFC1")
            error.config(text="")
            espIng=""
            if(len(l) ==1):
                for i in self.__palabrasEsp:
                    if(i[0] == l):
                        esp = i
                        ing = self.__diccionario.get(i)
                        espIng += f"{esp}-{ing}\n"
                        p.config(text=espIng)
                        p.pack()
                    else:
                        continue
            else:
                error.config(text="La letra no es válida")

            print("----- Se han buscado las palabras por letra -----")

        self.ventanaBuscarLet = Tk()
        self.ventanaBuscarLet.title(self.nombre)
        self.ventanaBuscarLet.geometry("467x500")
        self.ventanaBuscarLet.resizable(0, 0)
        self.labelFondo = Label(self.ventanaBuscarLet, bg="#B4E197", padx=467, pady=350)
        label = Label(self.ventanaBuscarLet, text="Buscar Palabras Por Letra", font=("Garamond", 28), bg="#99C4C8")

        label2 = Label(self.ventanaBuscarLet, text="Letra: ", font=("Gotham", 16), bg="#E5EFC1")
        letra = Entry(self.ventanaBuscarLet, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))
        buscar=Button(self.ventanaBuscarLet, text="Buscar", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                         pady=10, padx=10, relief=RIDGE, command=buscarLetra)
        error=Label(self.ventanaBuscarLet, text="", font=("Gotham", 16), bg="#E5EFC1", fg="#F32424")

        regresar=Button(self.ventanaBuscarLet, text="Regresar a Visualizar Palabras", font=("Constantia", 15), bg="#E5EFC1", fg="#383838",
                         pady=10, padx=10, relief=RIDGE, command=self.regresarPalLet)

        palabras = Frame(self.ventanaBuscarLet, padx=10, pady=10)

        label.place(x=40, y=10)
        label2.place(x=10, y=150)
        letra.place(x=80, y=150)
        buscar.place(x=340, y=140)
        error.place(x=10, y=185)
        palabras.place(x=10, y=230)
        self.labelFondo.place(x=0, y=0)
        regresar.place(x=10, y=65)
        self.ventanaBuscarLet.mainloop()

    def modificarP(self):
        self.nombre = "Modificar Palabra - Diccionario"
        self.ventanaP.destroy()

        def modificarValores():
            print("----- Modificar Palabras -----")
            esp=español.get().lower()
            ing=ingles.get().lower()
            palabrasEsp=self.__palabrasEsp
            if esp in palabrasEsp:
                print("----- Se han realizado los cambios -----")
                labelValores=" Cambios realizados "
                labelAgregar=f" {esp}-{ing} "
                labelP.config(text=labelValores)
                label2.config(text=labelAgregar)

                self.__diccionario[esp]=ing
                fichero.crearFichero()
                for i in self.__diccionario:
                    esp1=i
                    ing1=self.__diccionario.get(i)
                    fichero.escribirFichero(esp1, ing1)
            else:
                print("----- No se ha realizado ningún cambio -----")
                labelValores=" La palabra a modificar no existe."
                labelAgregar=" Puedes agregarla yendo al menú principal"
                labelP.config(text=labelValores)
                label2.config(text=labelAgregar)


        self.ventanaModificarP=Tk()
        self.ventanaModificarP.title(self.nombre)
        self.ventanaModificarP.geometry("467x350")
        self.ventanaModificarP.resizable(0, 0)
        self.labelFondo = Label(self.ventanaModificarP, bg="#68A7AD", padx=467, pady=350)

        label = Label(self.ventanaModificarP, text="Modificar Palabra", font=("Garamond", 28), bg="#68A7AD")

        labelEsp = Label(self.ventanaModificarP, text=" Palabra (Español) ", font=("Gotham", 16), bg="#E5EFC1")
        español = Entry(self.ventanaModificarP, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))
        labelIng = Label(self.ventanaModificarP, text="Modificar Traducción", font=("Gotham", 16), bg="#E5EFC1")
        ingles = Entry(self.ventanaModificarP, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))

        labelP = Label(self.ventanaModificarP, text=" - ", font=("Gotham", 16), bg="#E5EFC1", padx=10)
        label2 = Label(self.ventanaModificarP, text="  ", font=("Gotham", 16), bg="#E5EFC1", padx=10)

        agregar = Button(self.ventanaModificarP, text="Modificar Palabra", font=("Constantia", 15), bg="#E5EFC1",
                         fg="#383838", pady=10, padx=10, relief=RIDGE, command=modificarValores)

        regresar = Button(self.ventanaModificarP, text="Regresar a Principal", font=("Constantia", 15), bg="#E5EFC1",
                          fg="#383838", pady=10, padx=10, relief=RIDGE, command=self.regresarPrincipalModificar)

        label.place(x=100, y=10)
        self.labelFondo.place(x=0, y=0)
        labelEsp.place(x=10, y=80)
        español.place(x=200, y=80)
        labelIng.place(x=10, y=150)
        ingles.place(x=220, y=150)
        labelP.place(x=10, y=200)
        label2.place(x=10, y=230)
        agregar.place(x=245, y=280)
        regresar.place(x=20, y=280)
        self.ventanaModificarP.mainloop()


    def traducir(self):
        self.nombre = "Traducir - Diccionario"

        def traducirFrase():
            fr=frase.get()
            traduccion=[]
            palabras = fr.split()
            for y in range(len(palabras)):
                palabra = palabras[y]
                if (palabra in self.__palabrasEsp):
                    palabraIgual = self.__diccionario.get(palabra)
                    traduccion.insert(y, palabraIgual)
                    print("--", palabraIgual)
                else:
                    traduccion.insert(y, palabra)
                    print(palabra)

            fraseTraducida = " ".join(traduccion)
            labelFrase.config(text=fraseTraducida)
            print("----- Frase Traducida -----")

        self.ventanaTraducir = Tk()
        self.ventanaTraducir.title(self.nombre)
        self.ventanaTraducir.geometry("467x350")
        self.ventanaTraducir.resizable(0, 0)
        self.labelFondo = Label(self.ventanaTraducir, bg="#97C4B8", padx=467, pady=350)
        label = Label(self.ventanaTraducir, text="Traducir Español-Inglés", font=("Garamond", 28), bg="#DAE5D0")

        agregarPalabra = Label(self.ventanaTraducir, text=" Frase ", font=("Gotham", 16), bg="#E5EFC1")
        frase = Entry(self.ventanaTraducir, bg="#F3E9DD", fg="#383838", font=("Bickham script pro", 16))
        labelFrase=Label(self.ventanaTraducir, text="", font=("Gotham", 16), bg="#E5EFC1")
        boton = Button(self.ventanaTraducir, text="Traducir Frase", bg="#99C4C8", fg="#383838",
                                    highlightcolor="#557B83", font=("Gotham", 18), relief=RIDGE, command=traducirFrase)
        regresar = Button(self.ventanaTraducir, text="Regresar a Principal", font=("Constantia", 15), bg="#E5EFC1",
                          fg="#383838",
                          pady=10, padx=10, relief=RIDGE, command=self.regresarPrincipalTraducir)

        self.labelFondo.place(x=0, y=0)
        label.place(x=80, y=10)
        agregarPalabra.place(x=10, y=80)
        frase.place(x=90, y=80)
        labelFrase.place(x=10, y=200)
        boton.place(x=10, y=120)
        regresar.place(x=10, y=280)
        self.ventanaTraducir.mainloop()

    # Enlaces

    def regresarPrincipalAgregar(self):
        self.ventanaAgregarP.destroy()
        self.principal()

    def regresarPrincipalVisualizar(self):
        self.ventanaVisualizarP.destroy()
        self.principal()

    def irPrincipalVisualizar(self):
        self.ventanaP.destroy()
        self.visualizarP()

    def irTraducir(self):
        self.ventanaP.destroy()
        self.traducir()

    def regresarPrincipalTraducir(self):
        self.ventanaTraducir.destroy()
        self.principal()

    def regresarPrincipalModificar(self):
        self.ventanaModificarP.destroy()
        self.principal()

    def irPalabrasSinonimo(self):
        self.ventanaVisualizarP.destroy()
        self.buscarPalabrasSinonimo()

    def irPalabrasLetra(self):
        self.ventanaVisualizarP.destroy()
        self.buscarPalabrasLetra()

    def regresarPalSin(self):
        self.ventanaBuscarSin.destroy()
        self.visualizarP()

    def regresarPalLet(self):
        self.ventanaBuscarLet.destroy()
        self.visualizarP()


    # Métodos set y get

    def getPalabraEsp(self):
        return self.__palabraEspañol

    def setPalabraEsp(self, pespañol):
        self.__palabraEspañol=pespañol

    def getPalabraIng(self):
        return self.__palabraIngles

    def setPalabraIng(self, pingles):
        self.__palabraIngles=pingles

    def getDiccionario(self):
        return self.__diccionario


    # Métodos Fichero
    def agregarPFichero(self, esp, ing):
        self.setPalabraEsp(esp)
        self.setPalabraIng(ing)
        español=self.getPalabraEsp()
        ingles=self.getPalabraIng()
        fichero.escribirFichero(español, ingles)
        print("----- Se han agregado las palabras al fichero -----")