def chequing_3_cifras(num):
    return num in range(100, 1000)


resultado = chequing_3_cifras(343)

print(resultado)


def chequear_3_cifras(lista):
    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras


resultado = chequear_3_cifras([23, 440, 2000])
print(resultado)


# Ejemplo 1
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False

    return True


lista_numeros = [22, -55, 33, 12]


# Ejemplo 2
def suma_menores(lista_numeros):
    suma = 0

    for n in lista_numeros:
        if n in range(0, 1000):
            suma += n

    return suma


lista_numeros = [100, 500, -10, 1500, 999, 0, 450]


# Ejemplo 3
def cantidad_pares(lista_numeros):
    cuenta = 0

    for n in lista_numeros:
        if n % 2 == 0:
            cuenta += 1
    return cuenta


lista_numeros = [1, 2, 4, 5, 6, 7, 8, 9, 10]