# Si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\muina\\Desktop\\python_prueba\\funcion_nueva")

import Datos_suma_y_resta as resta
import Saludo_coscu as coscu



print(coscu.saludo("Lautaro","toro"))

print(resta.resta_total)

#print(sys.path)