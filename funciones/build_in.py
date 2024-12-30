numeros = [2,7 ,11,23,30]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# redondeando a 6 decimales
numero = round(12.223456, 2)
print(numero)


# retorna False -> 0, vacio,false, none // True -> distinto a 0,True, cadena, datos no vacio
resultado_bool = bool("asasaas")

#retorna true, si todos los valores son verdaderos
resultado_all = all([0,"true", [ 121, 242]])
print(resultado_all)