nombres = ["Ana", "Hugo", "Valeria"]
edades = [69, 17, 32]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre,edades,ciudades in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudades}")

# Ejemplo 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales,paises))

for capitales, paises in combinados:
    print(f"La capital de {paises} es {capitales}")

# Ejemplo 2
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portuges = ["um","dois","três","quatro","cinco"]
ingles = ["one","two","three", "four", "five"]

numeros = list(zip(espanol,portuges,ingles))