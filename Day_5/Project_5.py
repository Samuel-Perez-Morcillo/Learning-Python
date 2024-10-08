"""En esta ocasión el proyecto se tratra de diseñar el juego del ahorcado
    Como aun no contamos con la habilidad de dibujar el stickman, solo le
    pondremos al usuario que cuenta con 6 vidas para acertar la palabra
    que en primera instancia será representada por tantos guiones como letras
    tenga la palabra a acertar"""

from random import choice

palabras = ["infantil", "peregrino", "dermatologo", "massachusets", "lisboa", "samuelillo"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def palabra_a_adivinar(lista_palabras):
    palabra_aleatoria_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_aleatoria_elegida))
    return palabra_aleatoria_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra válida para el Juego")
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")

    print("  ".join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias, letras_unicas):
    fin = False

    if letra_elegida in palabra_oculta:
        if letra_elegida not in letras_correctas:
            letras_correctas.append(letra_elegida)
            coincidencias += palabra_oculta.count(letra_elegida)
    else:
        if letra_elegida not in letras_incorrectas:
            letras_incorrectas.append(letra_elegida)
            vidas -= 1

    if vidas == 0:
        fin = perder(palabra_oculta)
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder(palabra_oculta):
    print("Te Has Quedado Sin Vidas Sorry :( ")
    print(f"La palabra oculta era {palabra_oculta}")
    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Enhorabuena Has Encontrado La Palabra :)")
    return True


# Iniciar el juego
palabra, letras_unicas = palabra_a_adivinar(palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras Incorrectas: " + "-".join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    intentos, juego_terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos, letras_unicas)
