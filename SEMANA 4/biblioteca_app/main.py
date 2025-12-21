from modelos.libro import Libro    # Importamos la clase Libro desde modelos/libro.py
from modelos.usuario import Usuario # Importamos la clase Usuario desde modelos/usuario.py
from servicios.biblioteca import Biblioteca  # Importamos la clase Biblioteca desde servicios/biblioteca.py

# Definimos la función principal del programa
def main():
    biblioteca = Biblioteca()       # Creamos el objeto Biblioteca

    # Crear libro y usuario
    libro1 = Libro("Aprende a Programar", "Max Wainewright", "120")  # Creamos un libro con ISBN 120
    usuario1 = Usuario("Verónica", "2100662044")      # Creamos un usuario

    biblioteca.agregar_libro(libro1)                  # Agregamos el libro a la biblioteca

    print(biblioteca.prestar("120", usuario1))   # Prestamos el libro (debe funcionar)
    print(biblioteca.prestar("120", usuario1))   # Intentamos prestarlo otra vez (debe fallar)
    print(biblioteca.devolver("120"))                 # Devolvemos el libro (debe funcionar)
    print(biblioteca.prestar("120", usuario1))  # Lo prestamos otra vez (debe funcionar)
    print(biblioteca.prestar("500", usuario1))   # Probamos un ISBN que no existe

# Esto asegura que main() solo se ejecute si abrimos este archivo directamente
if __name__ == "__main__":
    main()                       # Ejecutamos la función principal
