frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola dalto"
numeros = (2, 5,7,8)

# evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")
    
print("-----------")
    
# evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
print("bucle terminado")

# recorriendo una cadena de texto
for letra in cadena:
    print(letra)

# for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
 # es igual a esto de abajo
# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)
    
print(numeros_duplicados)