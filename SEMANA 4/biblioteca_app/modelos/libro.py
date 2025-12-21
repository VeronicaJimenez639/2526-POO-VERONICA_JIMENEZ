# Definimos la clase Libro (representa un libro real de una biblioteca)
class Libro:
    # Constructor: se ejecuta cuando creamos un objeto Libro()
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo         # Guardamos el título del libro
        self.autor = autor           # Guardamos el autor del libro
        self.isbn = isbn             # Guardamos el ISBN
        self.prestado = False        # Estado inicial: no está prestado

    # Método para prestar el libro
    def prestar(self):
        if self.prestado:            # Si ya está prestado...
            return False             # ...no se puede prestar otra vez
        self.prestado = True         # Marcamos el libro como prestado
        return True                  # Confirmamos que sí se prestó

    # Método para devolver el libro
    def devolver(self):
        if not self.prestado:         # Si NO está prestado...
            return False              # ...no se puede devolver
        self.prestado = False         # Marcamos el libro como disponible
        return True                   # Confirmamos que sí se devolvió

    # Método especial para mostrar el libro como texto cuando hacemos print(libro)
    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"   # Texto según el estado
        return f"Libro({self.titulo}, {estado})"                # Devolvemos el texto final