#importando un modilo y asignandole el nombre "m_saludar"
# import modulo_saludar as m_saludar

# desde ese modulo le importamos 2 funciones
# from modulos_buenos.modulo_saludar import saludar,saludar_raro as saludo_kuka esto seria si modulo_saludar estuviera en otra carpeta
from modulo_saludar import saludar,saludar_raro as saludo_kuka

# Creamos las variables con los saludos
saludo = saludar("Lautaro")
saludo_raro = saludo_kuka('wachin')

# mostramos los resultados
print(saludo)
print(saludo_raro)

# para ver las propiedades y metodos de el namespace
# print(dir(m_saludar))