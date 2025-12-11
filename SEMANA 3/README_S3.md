## Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO)

En la versión de **programación tradicional** el programa está organizado solo con funciones. Primero se pide al usuario la temperatura de cada día de la semana, luego se calcula el promedio y al final se muestran los resultados. Todo se controla desde la función `main()`. Este enfoque es directo y funciona bien para problemas pequeños, porque la lógica es lineal y el código es corto.

En la versión con **Programación Orientada a Objetos (POO)** el problema se organiza usando clases y objetos, no solo funciones. Se usa la clase `ClimaDia` para representar un día con su temperatura y la clase `ClimaSemana` para manejar toda la semana. La clase `ClimaSemana` se encarga de pedir los datos, guardarlos y calcular el promedio mediante sus métodos. Además, el código POO está separado en varios archivos (`clima_dia.py`, `clima_semana.py` y `main_poo.py`), lo que hace que el proyecto quede más ordenado. 

Ambos enfoques calculan el mismo promedio semanal, pero la versión POO facilita agregar más características en el futuro sin que el código se vuelva tan desordenado.


