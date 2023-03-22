
from clases import Conventions
from clases import Case
from itertools import product, repeat
from random import choice

# from juego import HORIZONTAL, LONGITUDES_BARCOS, ORIENTACIONES

HORIZONTAL = 0
VERTICAL = 1
LONGITUDES_BARCOS = [2, 3, 3, 4, 4, 5]

ORIENTACIONES = (VERTICAL, HORIZONTAL)

instances = []
casillas_ocupadas = set()
# performance / legibilidad:
num_lineas = Conventions.tablero_num_lineas
num_columnas = Conventions.tablero_num_columnas
num2l = Conventions.generar_num_linea
num2c = Conventions.generar_num_columna

class Barco:
    casillas_ocupadas = set()
    def __init__(self, longitud):
        self.longitud = longitud
        self.orientacion = choice(ORIENTACIONES)
        self.tocado = False
        self.hundido = False

    def horizontal(self):
        if self.orientacion == HORIZONTAL:
            rang = choice(range(num_lineas))
            primero = choice(range(num_columnas + 1 - self.longitud))
            letra = num2l(rang)
            cifras = [num2c(x) for x in range(primero, primero + self.longitud)]
            self.casillas = {Case.Case.instances[l + c] 
                for l, c in product(repeat(letra, self.longitud), cifras)}
        else:
            rang = choice(range(num_columnas))
            primero = choice(range(num_lineas + 1 - self.longitud))
            cifra = num2c(rang)
            letras = [num2l(x) for x in range(primero, primero + self.longitud)]

            # Crear el barco
            self.casillas = {Case.instances[l + c]
                for l, c in product(letras, repeat(cifra, self.longitud))}
        return self.casillas

    def instanciar(self):
        inst = True
        for existente in instances:
            if self.casillas.intersection(existente.casillas):
                inst = False
                break
        if inst:
            # Agregar el barco en el contenedor de barcos
            instances.append(self)
            # Informar la casilla que contiene un barco.
            for casilla in self.casillas:
                casilla.contiene_barco = True
            # Agregar estas casillas a las casillas ocupadas :
            Barco.casillas_ocupadas.update(self.casillas)
            """print("Barco en: " + str(self.casillas))"""
                   
    def generar_barcos():
        while True:
            barco = Barco(choice(Conventions.barcos_longitud))
            barco.horizontal()
            barco.instanciar()
            if len(instances) == len(Conventions.barcos_longitud):
                break



        