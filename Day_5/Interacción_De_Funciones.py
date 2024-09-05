from random import shuffle

# Lista incial
palitos = ["-", "--", "---", "----"]


# Mezclar Palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista


# Pedirle Intento
def prueba_suerte():
    intento = ""

    while intento not in ["1", "2", '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)


# Comprobar Intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("A lavar los Platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento - 1]}")


# Comienzo del Juego

palitos_mezclados = mezclar_palitos(palitos)
seleccion_usuario = prueba_suerte()
chequear_intento(palitos_mezclados, seleccion_usuario)
