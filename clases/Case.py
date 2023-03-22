from numpy import product
# from juego import CASO_AGUA, CASO_NO_JUGADO, CASO_TOCADO
from clases.Conventions import (
  tablero_num_lineas,
  tablero_num_columnas,
  generar_num_linea,
  generar_num_columna,
  generar_nombre_casilla
)
	
CASO_NO_JUGADO = chr(0x2610)
CASO_TOCADO = chr(0x2611)
CASO_AGUA = chr(0x2612)
class Case:
  instances = {}
  jugadas = set()
  def __init__(self, x, y):
    # Adición de las coordenadas
    self.x = x
    self.y = y
    # Queremos poder acceder a una casilla a partir de sus coordenadas
    Case.instances[x, y] = self
    # Generación del nombre de la casilla
    self._generar_nombre()
    # Queremos poder acceder a una casilla a partir de su nombre
    Case.instances[self.nombre] = self

    #Evolución de la casilla
    self.jugada = False
    self.barco = None  # No toca a un barco de momento. 
    
  def _generar_nombre(self):
    """Este método puede ser sobrecargado fácilmente"""
    self.nombre = generar_nombre_casilla(self.x, self.y)
    
  def jugar(self):
    """Describe qué pasa cuando jugamos una casilla"""
    self.jugada = True
    self.jugadas.add(self)
    if self.barco is not None:
      if len(casillas - self.casillas_jugadas) == 0:
        print("Hundido !!")
      else:
        print("Tocado !")
    else:
        print("Agua !")
        
  def generar_casillas():
    for x in range(tablero_num_lineas):
      for y in range (tablero_num_columnas):
        Case(x, y)

  def __str__(self):
    """Sobrecarga del método de transformación en cadena"""
    if not self.jugada:
        return CASO_NO_JUGADO
    elif self.barco is None:
        return CASO_AGUA
    return CASO_TOCADO
