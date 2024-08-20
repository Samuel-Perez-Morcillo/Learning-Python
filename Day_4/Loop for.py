lista = ["a", "b", "c"]
for each in lista:
    numero_letra = lista.index(each) + 1
    print(f"letra {numero_letra}: {each}")


print("\n")
lista2 = ["Pablo", "Luis", "Fede", "Samu"]
for each in lista2:
    if each.startswith("L"):
        print(each)
    else:
        print(f"Nombre que no comienzan por L")


print("\n")
lista3 = [1, 2, 3, 4, 5]
mi_valor = 0
for each in lista3:
    mi_valor = mi_valor + each
    print(mi_valor)

print("\n")
palabra = "python"
for each in palabra:
    print(each)

print("\n")
dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
for each in dic.items():
    print(each)

print("\n")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0;
for each in lista_numeros:
    suma_numeros = suma_numeros + each;
    print(suma_numeros)

print("\n")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for each in lista_numeros:
    if (each % 2) == 0:
        suma_pares = suma_pares + each
    else:
        suma_impares = suma_impares + each

print(f"La suma de los numeros pares: {suma_pares}")
print(f"La suma de los numeros impares: {suma_impares}")