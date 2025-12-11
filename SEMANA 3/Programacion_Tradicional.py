#Progración tradicional: Promedio Semanal del Clima
#Este programa solicita al usuario las temperaturas diarias de una semana y calcula el promedio semanal utilizando funciones

def ingresar_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.

    Lógica:
    - Utiliza un bucle 'for' para iterar 7 veces.
    - Incluye manejo de errores (try-except) para asegurar que el usuario
      ingrese números válidos.

    Returns:
        list: Una lista de números flotantes con las temperaturas.
    """
    temperaturas = []     #Defino una lista vacía donde voy a guardar las temperaturas
    print("Ingreso de temperaturas diarias")   # Imprimo un título para que el usuario sepa qué va a hacer

    for i in range(7):    # Uso un for para repetir 7 veces (una por cada día de la semana)
        while True:       # Creo un ciclo infinito que solo termina cuando el usuario ingresa un dato válido
            try:
                entrada = float(input(f"Ingrese la temperatura del día {i+1}: "))
                temperaturas.append(entrada)   # Si la conversión fue correcta, se agrega la temperatura a la lista
                break #Sale del while si la entrada es correcta
            except ValueError:   # Si hubo error al convertir (por ejemplo escribió letras), entra al except
                print("Error: Por favor, ingrese un numero válido (use punto para decimales).")
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio aritmético de una lista de temperaturas.
    Args:
        temperaturas (list): Lista de valores numéricos (float o int).
    Returns:
        float: El promedio calculado. Retorna 0.0 si la lista está vacía.
    """
    if not temperaturas:   #Verifica si la lista está vacía
        return 0.0     # Si está vacía, devuelve 0.0 para evitar errores al dividir
    suma_total = sum(temperaturas)   #suma todos los elementos de la lista
    cantidad_dias = len(temperaturas)   #Devuelve cuántos elementos hay en la lista
    promedio = suma_total / cantidad_dias  #Fórmula del promedio aritmético
    return promedio     # Devuelve el promedio calculado


def main():
    """
    Función principal del programa.
    Aquí comienza la ejecución y se llaman las demás funciones.
    """
    datos_clima = ingresar_temperaturas_diarias()    #Primero obtenemos los datos
    promedio = calcular_promedio_semanal(datos_clima)  #Se procesan los datos
    print(f"\nResultados:")     #Se muestran los resultados
    print(f"Temperaturas ingresadas: {datos_clima}")
    print(f"El promedio semanal es: {promedio:.2f}°C")

if __name__ == "__main__":  # Bloque condicional para asegurar que main se ejecute solo si es el script principal
    main()










