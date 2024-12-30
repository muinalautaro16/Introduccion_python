numeros = [1,2,3,4,5,6,7,8,9]

# Creando una funcion lambda oara multiplicar por 2
multiplicar_por_dos = lambda X : X*2

#Creando una funcion que diga si es par o no
# def es_par(num):
#     if(num%2==0):
#         return True
   
# usando filter con una funcion comun
 

# print(multiplicar_por_dos(5))

# Creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))