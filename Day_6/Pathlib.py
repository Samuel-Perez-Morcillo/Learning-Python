from pathlib import Path, PureWindowsPath

# Rutas Relativas
carpeta = Path("/Users/samuelperez/Desktop/Carpeta_Ruta_Alternativa_Python/Prueba_copia.txt")
print(carpeta.read_text())  # nos muestra el contenido del archivo
print(carpeta.suffix)  # nos muestra la extension del archivo
print(carpeta.stem)  # nos muestra el nombre pero sin la terminación

# Tambien podremos comprobar directamente si el archivo en cuestion existe

if carpeta.exists():
    print("Este Archivo Existe")
else:
    print("No existe")

rutaWindowsPath = PureWindowsPath(carpeta)  # Esto se usa para traducir una ruta de mac a Windows


# Para tener una ruta absoluta del directorio en el que estamos

base = Path.home()
print(base)

guia = Path(base, "Hola", "Quetal.txt")
print(guia)