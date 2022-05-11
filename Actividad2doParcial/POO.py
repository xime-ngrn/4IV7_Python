import math

class FiguraGeo():
    def __init__(self):
        self.area=0
        self.perimetro=0


class Figura2Parametros(FiguraGeo):
    def __init__(self):
        super().__init__()

    def areaTriangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area=self.base*self.altura/2
        return self.area

    def areaRectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area=self.base*self.altura
        return self.area

    def perimetroRectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.perimetro=(self.base * 2) + (self.altura * 2)
        return self.perimetro


class Figura1Parametro(FiguraGeo):
    def __init__(self):
        super().__init__()

    def areaCirculo(self, parametro):
        self.parametro=parametro
        self.area=math.pi*(self.parametro**2)
        return self.area

    def perimetroCirculo(self, parametro):
        self.parametro = parametro
        self.perimetro=math.pi*2*self.parametro
        return self.perimetro

    def areaCuadrado(self, parametro):
        self.parametro = parametro
        self.area=self.parametro**2
        return self.area

    def perimetroCuadrado(self, parametro):
        self.parametro = parametro
        self.perimetro=self.parametro*4
        return self.perimetro

        # si el triangulo es equilatero
    def perimetroTriangulo(self, parametro):
        self.parametro = parametro
        self.perimetro = self.parametro * 3
        return self.perimetro