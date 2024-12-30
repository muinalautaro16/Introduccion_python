with open("archivos\\python.txt.txt", 'a', encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"oracion {i+1} agregada \n")