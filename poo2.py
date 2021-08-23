
class Usuario:

    cantidad_usuarios = 100

    def __init__(self, nombre, apellido, edad, persona_masculina):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.persona_masculina = persona_masculina
        self.premium = False

    def __repr__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad}, {self.persona_masculina}, {self.premium}"

    def __del__(self):
        print("Objeto borrado")


    def convetir_premium(self):
        self.premium = True
    
    def mirar_peliculas(self):
        if self.premium:
            print("El usuario puede ver las peliculas")
        else:
            print("El usuario no es premium")

    @staticmethod
    def usuario_mayor(edad):
        return edad >= 18

    @classmethod
    def cantidad_usuarios(cls):
        return cls.cantidad_usuarios

#Usuario.cantidad_usuarios()

usuario = Usuario("Gaston", "Fenske", 21, True)
print(usuario)
print(usuario.premium)
usuario.mirar_peliculas()
usuario.convetir_premium()
print(usuario)
print(usuario.premium)
usuario.mirar_peliculas()


print(Usuario.usuario_mayor(18))

