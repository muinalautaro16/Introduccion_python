# #para crear una funcion simple se utiliza def()
# def saludar():
#     print("Hola wacho, como estas?")
    
# saludar() # asi se ejecuta la funcion simple

# crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else: 
        adjetivo = "crack" 
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")
    
saludar("lautaro", "hombre")


#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefgj"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = -2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña 

password = crear_contraseña_random(3)
frase = f"Tu contrasela nueva es: {password}"
print(frase)
    