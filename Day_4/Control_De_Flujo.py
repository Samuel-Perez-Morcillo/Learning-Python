if 10 < 9:
    print("Es Correcto")
else:
    print("No es correcto")


mascota = "Canguro"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No se que animal tienes")


edad = 16
nota = 8

if edad < 18:
    print("Eres menor de edad")
    if nota >= 5:
        print("Aprobado")
    else:
        print("Suspenso")
elif edad == 18:
    print("justo ahora eres mayor de edad")
else:
    print("Eres un mayor de edad")