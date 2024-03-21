import subprocess

def generar(contenido, salida):
    try:
        # Definimos la ruta completa al ejecutable dot
        ruta_dot = "./lib/graphviz/bin/dot"

        # Definimos las rutas completas de los archivos
        archivodot = "./util/dot/grafica.dot"

        # Creamos y escribimos en el archivo
        with open(archivodot, "w") as file:
            file.write(contenido)

        # Construimos el comando y lo ejecutamos
        comando = [ruta_dot, "-Tsvg", archivodot, "-o", salida]
        subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    except Exception as e:
        print(e)