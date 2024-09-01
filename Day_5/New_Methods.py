# Método Lstrip()
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
x = texto.lstrip(",:%_#")
print(x)

# Método Insert
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(4,"naranja")
print(frutas)


# Método IsdisJoin
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)