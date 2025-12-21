# Definimos la clase Usuario (representa a una persona que pide libros)
class Usuario:
    # Constructor: se ejecuta cuando creamos un objeto Usuario()
    def __init__(self, nombre, cedula):
        self.nombre = nombre          # Guardamos el nombre del usuario
        self.cedula = cedula          # Guardamos la cédula del usuario

    # Método especial para mostrar el usuario como texto cuando hacemos print(usuario)
    def __str__(self):
        return f"Usuario({self.nombre})"  # Devolvemos un texto simple del usuario