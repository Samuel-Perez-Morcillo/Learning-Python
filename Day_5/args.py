def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(5, 6, 4))


# De forma mas sencilla y real el mismo ejercicio

def suma2(*args):
    return sum(args)


print(suma2(4, 5, 6))


# Ejemplo 2

def suma_cuadrados(*args):
    suma = 0

    for n in args:
        numero = n ** 2
        suma += numero
    return suma


# Ejemplo 3

def numeros_persona(nombre, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n

    return f"{nombre}, la suma de tus numeros es {suma_numeros}"
