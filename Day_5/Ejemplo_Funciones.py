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
