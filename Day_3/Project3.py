# Crea un analizador de texto

print("Hola, Bienvenido al Analizador de Texto\n")
texto = input("Introduzca el Texto que quiere analizar : \n")

letra1 = input("Introduzca 1 letra a buscar sus repeticiones en el texto: ")
letra2 = input("Introduzca otra letra a buscar sus repeticiones en el texto: ")
letra3 = input("Introduzca una ultima letra a buscar sus repeticiones en el texto: ")

analizador_de_letras = {
    "clave1": letra1,
    "clave2": letra2,
    "clave3": letra3
}
"\n"

repeticiones1 = texto.count(analizador_de_letras["clave1"])
repeticiones2 = texto.count(analizador_de_letras["clave2"])
repeticiones3 = texto.count(analizador_de_letras["clave3"])
"\n"

print(f"Su texto contiene la letra ({letra1}) {repeticiones1} veces")
print(f"Su texto contiene la letra ({letra2}) {repeticiones2} veces")
print(f"Su texto contiene la letra ({letra3}) {repeticiones3} veces \n")

"\n"

print("A continuación le Brindaremos unos datos sobre su texto de forma adicional\n")
contador = len(texto)
primera_letra = texto[0]
ultima_letra = texto[-1]
texto_Alrevés = texto[::-1]
buscador_de_palabra = "python" in texto

print(f"Su texto tiene {contador} letras incluyendo espacios")
print(f"Su primera letra en el texto es la letra {primera_letra}")
print(f"Si ultima letra en el texto es la letra {ultima_letra}")
print(f"El texto introducido del revés seria [ {texto_Alrevés} ]")
print(f"Aparece la palabra Phyton en el texto?, la respuesta es {buscador_de_palabra}")




