# Solución sencilla al proyecto 3
print("Bienvenido a tu Analizador de Textos")

texto = input("Ingresa el texto que deseas analizar: ")
texto = texto.lower()

letras = []
letras.append(input("Ingresa la primera letra para ver cuantas veces se encuentra repetida: ").lower())
letras.append(input("Ingresa la segunda letra para ver cuantas veces se encuentra repetida: ").lower())
letras.append(input("Ingresa la tercera letra para ver cuantas veces se encuentra repetida: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Tu letra {letras[0]} se repite en el texto {cantidad_letras1} veces")
print(f"Tu letra {letras[1]} se repite en el texto {cantidad_letras2} veces")
print(f"Tu letra {letras[2]} se repite en el texto {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} cantidad de palabras en el texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial de tu texto es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Tu texto invertido seria asi : \n '{texto_invertido}'")


print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra python {dic[buscar_python]} se encuentra en tu texto")
