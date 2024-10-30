# Este proyecto tratará de crear una especie de adivinador en la que el cliente
# deberá intentar el numero que nosotros hemos pensado con un numero del 1 al 100
# El cliente solo tendra 8 intentos y siempre deberá ingresar un numero que este en
# el rango a adivinar.

from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1, 100)
nombre_usuario = input("Dime tu nombre: ")

print(f"Bienvenido {nombre_usuario} al juego de Adivina el número\n")
print("Deberás ingresar un numero del 1 al 100 y solo dispondrás de 8 intentos")

while intentos < 8:
    estimado = int(input("Cual es el Número ?: "))
    intentos += 1

    if estimado < 1:
        print(f"El numero que has puesto es inferior a 1 y has perdido un intento te quedan {8 - intentos} intentos")
    elif estimado > 100:
        print(
            f"El numero que has ingresado es superior a 100 y has perdido un intento te quedan {8 - intentos} intentos")
    elif estimado < numero_secreto:
        print("Mi número es más alto")
    elif estimado > numero_secreto:
        print("Mi numero es más bajo")
    else:
        print(f"HAS ACERTADO ENHORABUENA {nombre_usuario} solo te ha tomado {intentos} intentos ")
        break;

if estimado != numero_secreto:
    print(f"Se te han acabado los intentos, LOSIENTO \n El numero secreto era {numero_secreto}")
