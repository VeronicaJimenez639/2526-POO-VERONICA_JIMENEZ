# Archivo: clima_semana.py
# Clase que representa el clima de toda una semana.

from clima_dia import ClimaDia  # importamos la clase del otro archivo

class ClimaSemana:
    """
    Clase que representa el clima de toda una semana.
    Trabaja internamente con varios objetos de tipo ClimaDia.
    """
    def __init__(self):
        # Lista privada donde se guardan los 7 días de la semana
        self.__dias= [
            ClimaDia("Lunes"),   # Cada elemento es un objeto de la clase ClimaDia.
            ClimaDia("Martes"),
            ClimaDia("Miércoles"),
            ClimaDia("Jueves"),
            ClimaDia("Viernes"),
            ClimaDia("Sabado"),
            ClimaDia("Domingo")
        ]

    def ingresar_datos(self):
        """
        Pide al usuario la temperatura para cada día y la guarda en los objetos ClimaDia.
        """
        print("Ingreso de temperaturas de la semana")
        for dia in self.__dias:  # Recorremos la lista de días (objetos ClimaDia)
            while True:
                try:
                    # Pedimos la temperatura para el día actual
                    dato = float(input(f"Ingrese la temperatura del {dia.nombre_dia} en °C: "))
                    dia.establecer_temperatura(dato)  # Guardamos la temperatura usando el método del objeto
                    break  # Si todo salió bien, salimos del while
                except ValueError:
                    # Si el usuario escribe algo que no es número, mostramos un mensaje de error
                    print("Error:Ingrese un número válido (use punto para decimales).")

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas de todos lso días.
        """
        if len(self.__dias) == 0:   # Si por alguna razón la lista está vacía, devolvemos 0.0
            return 0.0

        # Sumamos las temperaturas de cada objeto ClimaDia
        suma = 0.0
        for dia in self.__dias:
            suma += dia.obtener_temperatura()

        # Calculamos el promedio dividiendo entre la cantidad de días
        promedio = suma / len(self.__dias)
        return promedio

    def mostrar_resumen(self):
        """
        Muestra todas las temperaturas registradas en la semana.
        """
        print("\nTemperaturas registradas en la semana:")
        for dia in self.__dias:   #Gracias a __str__ puedo imprimir el objeto directo
            print(" -", dia)