def multiplicar(numero1, numero2):
    return numero1 * numero2


resultado = multiplicar(5, 10)
print(resultado)

# Ejemplo 1
def usd_a_eur(dolares):
    return dolares * 0.90

dolares = 5

print(usd_a_eur(dolares))

# Ejemplo 2
def invertir_palabra(palabra):
    return palabra[::-1].upper()


palabra = "Marta"
print(invertir_palabra(palabra))