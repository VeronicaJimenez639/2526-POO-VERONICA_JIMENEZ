# Archivo: clima_dia.py
# Clase que representa la información de un solo día de clima.

class ClimaDia:
    """
    Representa un día de la semana con su temperatura.
    """
    def __init__(self, nombre_dia):
        """
        Constructor de la clase.
        Aquí se crean los atributos iniciales del objeto.
        """
        # Guardo el nombre del día (por ejemplo: "Lunes", "Martes", etc.)
        self.nombre_dia = nombre_dia  # Atributo privado donde guardaré la temperatura del día.
        self.temperatura = 0.0   # Empieza en 0.0 hasta que el usuario ingrese un valor real.

    def establecer_temperatura(self, valor):
        """
        Guarda la temperatura en el atributo privado.
        """
        self.__temperatura = valor

    def obtener_temperatura(self):
        """
        Devuelve la temperatura almacenada.
        """
        return self.__temperatura

    def __str__(self):
        """
        Este método le dice a Python qué texto mostrar cuando usamos print() con un objeto de esta clase.
        """
        return f"{self.nombre_dia}: {self.__temperatura:.2f} °C"