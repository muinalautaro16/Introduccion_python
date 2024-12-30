#Forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados

# resultado = suma([5,3,9,5,12])

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([5,3,9,5,12])
print(resultado2)


# lo mismo que arriba pero Utilizando el operador * como argumento args
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}" 

resultado = suma("Lautaro",5,3,9,5,12)
print(resultado)