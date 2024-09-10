lista_cafes = [("capuccino", 1.5), ("Moha", 2.4), ("Expresso", 1.73), ("Latte", 1.20)]


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass

    return cafe_caro, precio_mayor


cafe, precio = cafe_mas_caro(lista_cafes)

print(f"El cafe mas caro es el {cafe} que cuesta {precio} €")

# Ejemplo 2
from random import randint


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(Uno, Dos):
    suma_dados = (Uno + Dos)

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados <= 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


Dado1, Dado2 = lanzar_dados()
resultado = evaluar_jugada(Dado1, Dado2)
print(resultado)


# Ejemplo 3
lista_numeros = [1, 2, 3, 3, 1, 3, 9, 4]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.remove(max(lista))

    return lista


def promedio(lista):
    if len(lista) > 0:
        resultado = sum(lista) / len(lista)
    else:
        resultado = 0

    return resultado


lista_reducida = reducir_lista(lista_numeros)
promedio_resultado = promedio(lista_reducida)

# Ejemplo 4
from random import choice

lista_numeros = [2, 5, 7, 9, 21]


def lanzar_moneda():
    return choice(["Cara", "Cruz"])


def probar_suerte(lanzamiento, lista):
    if lanzamiento == "Cara":
        lista.clear()
        return lista
    else:
        return lista

def probar_suerte():
    moneda = lanzar_moneda()
    conseguir_lista = probar_suerte(moneda, lista_numeros)