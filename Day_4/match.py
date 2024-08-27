serie = "N-02"
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Alcatel")

# Ejemplo 1

cliente = {"nombre": "Federico",
           "edad": 45,
           "ocupacion": "instructor"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reaves",
                              "director": "Lana Rhoades"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un Cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Es una Película")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
