# Creando un conjunto con set()
conjunto = set(["Dato1", "Dato2"])

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato3", "Dato4"])
conjunto2 = {conjunto1, "dato5"}
print(conjunto2)



# Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# verificando si es un subconjunto
#resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
# print(resultado)

# verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1


# Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)