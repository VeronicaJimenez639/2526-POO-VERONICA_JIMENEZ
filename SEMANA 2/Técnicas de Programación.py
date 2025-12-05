#EJEMPLO DE TÉCNICAS DE PROGRAMACIÓN
# Abstracción, Encapsulación, Herencia y Polimorfismo
# Contexto: Cuentas bancarias

#CLASE BASE

class CuentaBancaria:
    # Método constructor: se ejecuta al crear una nueva cuenta
    def __init__(self, titular, saldo_inicial, tasa_interes):
        # Atributos del objeto. Guardan el estado de la cuenta.
         self.titular = titular          # Nombre de la persona dueña de la cuenta
         self._saldo = saldo_inicial     # Saldo actual de la cuenta (atributo protegido)
         self._tasa_interes = tasa_interes  # Tasa de interés anual en porcentaje

    # Representa ABSTRACCIÓN porque muestra en pantalla los datos más importantes de la cuenta
    def mostrar_datos(self) :
        print(f"\nCuenta de: {self.titular}")      # Imprime el nombre del titular
        print(f"Saldo actual: {self._saldo} dólares")  # Imprime el saldo actual
        print(f"Tasa de interés: {self._tasa_interes}%") # Imprime la tasa de interés

    # Suma un monto al saldo de la cuenta (depósito)
    def depositar(self, monto):
        self._saldo += monto          # Aumenta el saldo
        print(f"{self.titular} depositó {monto} dólares.")  # Mensaje de confirmación

    # Resta un monto del saldo de la cuenta (retiro), si hay dinero suficiente
    def retirar(self, monto):
        if monto <= self._saldo:  # Verifica si el saldo alcanza
            self._saldo -= monto  # Disminuye el saldo
            print(f"{self.titular} retiró {monto} dólares.") # Mensaje de retiro exitoso
        else:
            # Si no hay suficiente saldo, muestra un mensaje de error
            print(f"{self.titular} no tiene saldo suficiente.")

    # Calcula el interés anual según el saldo y la tasa de interés
    def calcular_interes_anual(self):
        return self._saldo * (self._tasa_interes / 100) # Fórmula del interés

    # Aplica el interés anual a la cuenta (lo suma al saldo)
    def aplicar_interes(self):
        interes = self.calcular_interes_anual() # Llama al método que calcula el interés
        self._saldo += interes                  # Suma el interés al saldo
        # Muestra cuánto interés se aplicó, con dos decimales
        print(f"Se aplicaron {interes:.2f} dólares de interés a la cuenta de {self.titular}.")

#HERENCIA: CuentaAhorros hereda de CuentaBancaria

class CuentaAhorros(CuentaBancaria):
    # Redefine el cálculo de interés (POLIMORFISMO)
    def calcular_interes_anual(self):
        return self._saldo * (self._tasa_interes / 100) # En la cuenta de ahorros se usa la tasa completa

# HERENCIA: CuentaCorriente también hereda de CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    # Constructor propio de CuentaCorriente
    def __init__(self, titular, saldo_inicial, tasa_interes, costo_mantenimiento):
        # Llama al constructor de la clase padre (CuentaBancaria)
        super().__init__(titular, saldo_inicial, tasa_interes)
        # Atributo extra: costo de mantenimiento de la cuenta
        self._costo_mantenimiento = costo_mantenimiento

    # Resta del saldo el costo de mantenimiento
    def cobrar_mantenimiento(self):
        self._saldo -= self._costo_mantenimiento  # Descuenta el mantenimiento del saldo
        # Mensaje indicando cuánto se cobró y a quién
        print(f"Se cobró {self._costo_mantenimiento} dólares de mantenimiento a {self.titular}.")

    # Redefine el cálculo de interés (POLIMORFISMO)
    def calcular_interes_anual(self):
        # En la cuenta corriente el interés es menor (mitad de la tasa)
        return self._saldo * ((self._tasa_interes / 2) / 100)

#FUNCIÓN DE OPERACIONES: : recibe dos cuentas y realiza movimientos
def simular_operaciones(cuenta1, cuenta2):
    print("\n INICIO DE OPERACIONES ")
    # Muestra los datos iniciales de ambas cuentas
    cuenta1.mostrar_datos()
    cuenta2.mostrar_datos()

    print("\n Depósitos")
    cuenta1.depositar(200) # Depósito de 200 en la primera cuenta
    cuenta2.depositar(100) # Depósito de 100 en la segunda cuenta

    print("\n Retiros")
    cuenta1.retirar(50)  # Retiro de 50 en la primera cuenta
    cuenta2.retirar(300)   # Retiro de 300 en la segunda cuenta

    # Si la segunda cuenta es una CuentaCorriente, se cobra mantenimiento
    if isinstance(cuenta2, CuentaCorriente):
        print("\n Cobro de mantenimiento")
        cuenta2.cobrar_mantenimiento()   # Llama al método específico de CuentaCorriente

    # Aplicación de intereses en ambas cuentas
    print("\n Aplicación de intereses")
    cuenta1.aplicar_interes()   # Aplica interés según el tipo de cuenta1
    cuenta2.aplicar_interes()    # Aplica interés según el tipo de cuenta2

    # Muestra el estado final de las cuentas después de todas las operaciones
    print("\n Estado final")
    cuenta1.mostrar_datos()
    cuenta2.mostrar_datos()

    print("\n FIN DE OPERACIONES")

# PRUEBA DEL SISTEMA: aquí se crean los objetos y se llama a la función
# Crea una CuentaAhorros con titular "Verónica", saldo 1000 y tasa 5%
cuenta_ahorros = CuentaAhorros("Verónica", saldo_inicial=1000, tasa_interes=5)

# Crea una CuentaCorriente con titular "Andrea", saldo 500, tasa 3% y mantenimiento de 10
cuenta_corriente = CuentaCorriente("Andrea", saldo_inicial=500, tasa_interes=3, costo_mantenimiento=10)

# Llama a la función que simula todas las operaciones entre ambas cuentas
simular_operaciones(cuenta_ahorros, cuenta_corriente)


