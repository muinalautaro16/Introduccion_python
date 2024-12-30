# creando diccionarios con dict
diccionario = dict(nombre="lucas", apellido="dalto")

# las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jajaja"}


# Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

# Creando diccionarios con fromkeys() cambiando el valor por defecto a " nose"
diccionario = dict.fromkeys(["nombre", "apellido"], "nose")

print(diccionario)