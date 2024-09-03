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