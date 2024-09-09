def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=10, y=20, j=10))


# También Podemos Combinar todo lo aprendido en los parámentros

def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segudno valor es {num2}")

    for n in args:
        print(f"args = {n}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100, 20, 30, 50]
kwargs = {"x": "uno", "y": "2", "j": "tres"}

prueba(2, 5, *args, **kwargs)


# Ejemplo 1
def cantidad_atributos(**kwargs):
    total_args = 0

    for clave, valor in kwargs.items():
        total_args += 1

    return total_args


# Ejemplo 2
def lista_atributos(**kwargs):
    valores = []

    for clave, valor in kwargs.items():
        valores.append(valor)

    return valores
