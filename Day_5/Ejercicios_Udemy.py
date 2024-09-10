def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3

    if suma > 15:
        print("Al resultar la suma mayor a 15 se muestra el numero máximo que has ingresado: ")
        return print(max(num1, num2, num3))
    elif suma < 10:
        print("Al resultar la suma menor a 10 se muestra el numero minimo que has ingresado: ")
        return print(min(num1, num2, num3))
    else:
        print("Al resultar la suma entre 10 y 15 incluidos se muestra el numero intermedio que has ingresado: ")
        return print(sorted([num1, num2, num3])[1])


num1 = int(input("Ingresa el primer numero a sumar: "))
num2 = int(input("Ingresa el segundo numero a sumar: "))
num3 = int(input("Ingresa el tercer numero a sumar: "))

devolver_distintos(num1, num2, num2)


# Ejercicio 2

def palabra_del_reves(palabra):
    letras_unicas = set(palabra.lower())
    resultado = sorted(letras_unicas)
    return resultado


prueba = "Monja"
print(palabra_del_reves(prueba))


# Ejercicio 3
def doble_cero(*args):
    for n in range(len(args) - 1):
        if args[n] == 0 and args[n + 1] == 0:
            return True
    return False


print(doble_cero(1, 2, 34, 5, 5, 6, 7, 1, 0, 0))


# Ejercicio 4

def contar_pares_impares(num):
    contador_pares = 0
    contador_impares = 0
    for n in range(0, num + 1):
        if n % 2 == 0 and n != 0:
            contador_pares += 1
        elif n % 2 != 0 and n != 1:
            contador_impares += 1
    return print(f"Hasta el numero {num}, Hay {contador_pares} primos y {contador_impares} impares")


print(contar_pares_impares(6))


# Ejercicio 5
def es_primo(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def contar_primos(limite):
    contador = 0
    for num in range(limite + 1):
        if es_primo(num):
            print(num)
            contador += 1
    print(f"Cantidad de numeros primos encontrados: {contador}")
    return contador


print(contar_primos(8))
