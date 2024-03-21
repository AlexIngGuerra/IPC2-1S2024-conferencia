

def generar(contenido, salida):
    try:
        # Definir ruta dot
        ruta_dot = "./libs/graphviz/bin/dot"

        # Definimos ruta de archivo dot
        archivo_dot = "./util/dot/grafica.dot"

        # Creamos el archivo
        with open(archivo_dot, "w") as file:
            file.write(contenido)

            
    except Exception as e:
        print(e)