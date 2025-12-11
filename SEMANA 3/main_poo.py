# Archivo: main_poo.py
# Versión POO del promedio semanal del clima.
# Aquí solo usamos las clases definidas en otros archivos.

from clima_semana import ClimaSemana   # Importamos la clase ClimaSemana desde clima_semana.py

def main():
    """
    Función principal del programa.
    Aquí creo el objeto ClimaSemana y llamo a sus métodos.
    """
    clima_semana = ClimaSemana()    # Creo un objeto de la clase ClimaSemana
    clima_semana.ingresar_datos()   # El objeto se encarga de pedir las temperaturas al usuario
    promedio = clima_semana.calcular_promedio() # Luego calculamos el promedio semanal usando un método del objeto

    print("\n Informe Semanal")    # Finalmente mostramos la información y el promedio
    clima_semana.mostrar_resumen()
    print(f"\nPromedio semanal de temperaturas: {promedio:.2f} °C")

# Bloque para que main() se ejecute solo si este archivo es el programa principal
if __name__ == "__main__":
    main()