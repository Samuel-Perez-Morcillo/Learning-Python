# Es importante saber que los bucles while deben tener una condición que haga que
# el bucle no se repita infinitas veces

print("\n")
monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

print("\n")
respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print("gracias")

print("\n")
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

print("\n")
# Break//Continue//Pass// son importantes en los bucles

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for each in lista_numeros:
    if each < 0:
        break
    else:
        print(each)
