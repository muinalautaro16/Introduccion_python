# Falto el profesor y los piber van a armar la clase

# Pedir el nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_compañeros(cantidad_de_compañeros):
    #Creando la lista con los compañeros
    compañeros = []
    
    # Ejecutando un for para pedir la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese los nombres: ')
        edad = int(input("Ingrese la edad: "))
        compañero = (nombre,edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
        
    #Ordenandolos de menor a mayor segun su edad    
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    # para definir al asistente y al profesor
    asistente = compañeros[0][0]    
    profesor = compañeros[-1][0]
    
    # Retornamos una tupla
    return asistente,profesor

# desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(3)

# mostramos el resultado
print(f"el asistente es: {asistente}, y el profesor es: {profesor}")