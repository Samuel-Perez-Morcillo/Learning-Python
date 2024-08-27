palabra = "python"
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Una forma mas sencilla de realizarlo seria :
palabra = "python"
lista = [letra for letra in palabra]
print(lista)

# Ejemplo 1
lista = [n if n * 2 > 10 else "no" for n in range(0, 21, 2)]
print(lista)

# Ejemplo 2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]

# Ejemplo 3
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2==0]

# Ejemplo 4
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]