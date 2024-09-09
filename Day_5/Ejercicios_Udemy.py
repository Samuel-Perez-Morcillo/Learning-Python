def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3

    if suma > 15:
        print("Al resultar la suma mayor a 15 se muestra el numero máximo que has ingresado: ")
        return print(max(num1, num2, num3))
    elif suma < 10:
        print("Al resultar la suma menor a 10 se muestra el numero minimo que has ingresado: ")
        return print(min(num1, num2, num3))
    elif 10 >= suma >= 15:
        print("Al resultar la suma entre 10 y 15 incluidos se muestra el numero intermedio que has ingresado: ")
        return sorted(num1, num2, num3)


num1 = int(input("Ingresa el primer numero a sumar: "))
num2 = int(input("Ingresa el segundo numero a sumar: "))
num3 = int(input("Ingresa el tercer numero a sumar: "))

devolver_distintos(num1, num2, num2)

