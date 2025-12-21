# Definimos la clase Biblioteca (administra libros y préstamos)
class Biblioteca:
    # Constructor: se ejecuta cuando creamos Biblioteca()
    def __init__(self):
        self.libros = []               # Creamos una lista vacía para guardar libros

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)      # Añadimos el objeto libro a la lista

    # Método para prestar un libro según su ISBN a un usuario
    def prestar(self, isbn, usuario):
        for libro in self.libros:      # Recorremos todos los libros guardados
            if libro.isbn == isbn:     # Recorremos todos los libros guardados
                if libro.prestar():    # Intentamos prestar (usa el método del Libro)
                    return f"Libro prestado a {usuario.nombre}."   # Mensaje de éxito
                return "El libro ya está préstado."                # Si no se pudo prestar
        return "Libro no encontrado."                              # Si no existe el ISBN

    # Método para devolver un libro según su ISBN
    def devolver(self, isbn):
        for libro in self.libros:      # Recorremos los libros guardados
            if libro.isbn == isbn:     # Si encontramos el ISBN...
                if libro.devolver():   # Intentamos devolver (método del Libro)
                    return "Libro devuelto con éxito."        # Mensaje de éxito
                return "El libro ya estaba disponible."       # Si ya estaba disponible
        return "Libro no encontrado."                         # Si no existe el ISBN