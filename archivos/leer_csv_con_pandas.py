# CSV ( valores separados por comas)
import pandas as pd

# Usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")

# obteniendo los datos de la columna nombre
nombres = df["nombre"]

# usando slice antes del : es donde empieza y despues en donde termina
# cadena = "0123456789"
# print(cadena[:5])

# ordenando el dataframe por la edad
df_ordenado = df.sort_values('edad')
print(df_ordenado)