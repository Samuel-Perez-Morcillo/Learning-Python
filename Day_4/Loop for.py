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


