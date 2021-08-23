
class Catalogo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []


class Pelicula:

    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __repr__(self):
        return f"{self.nombre}, {self.duracion}, {self.genero}"


catalogo1 = Catalogo("Catalogo de terror")
pelicula = Pelicula("Actividad Paranormal", 120, "terror")

print(catalogo1.peliculas)
catalogo1.peliculas.append(pelicula)
print(catalogo1.peliculas)
print(catalogo1.peliculas[0])
print(catalogo1.peliculas[0].nombre)