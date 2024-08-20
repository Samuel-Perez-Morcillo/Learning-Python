# Es importante saber que los bucles while deben tener una condición que haga que
# el bucle no se repita infinitas veces

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")


respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print("gracias")

# Break//Continue//Pass// son importantes en los bucles