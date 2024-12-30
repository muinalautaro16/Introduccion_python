animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = (23, 54,76,86)

for numero in numeros:
    resultado = numero * 10
    print(resultado)

for animal in animales:
    print(animal)
    
    
for numero, animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    

for num in range(10, 20):
    print(num)
 
# forma no optima de recorrer una lista con su indice   ( no funciona en conjuntos) 
for num in range(len(numeros)):
    print(numeros[num])
    
# forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    

# usando el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
# todo lo anterior funcion exactamente igual para tuplas, listas y conjuntos
