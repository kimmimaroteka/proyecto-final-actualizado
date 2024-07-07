import pickle
from datetime import datetime

class Transaccion:
    def __init__(self, monto, fecha, descripcion, tipo):
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion
        self.tipo = tipo

    def __repr__(self):
        return f"{self.fecha} - {self.tipo} - {self.descripcion}: ${self.monto:.2f}"

class GestorFinanciero:
    def __init__(self):
        self.transacciones = []
        self.cargar_datos()

    def agregar_transaccion(self, monto, fecha, descripcion, tipo):
        nueva_transaccion = Transaccion(monto, fecha, descripcion, tipo)
        self.transacciones.append(nueva_transaccion)
        print("Transacción agregada exitosamente.")

    def listar_transacciones(self):
        for transaccion in sorted(self.transacciones, key=lambda x: x.fecha):
            print(transaccion)

    def calcular_balance(self):
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'Ingreso')
        gastos = sum(t.monto for t in self.transacciones if t.tipo == 'Gasto')
        ahorro = ingresos - gastos
        print(f"Ingresos Totales: ${ingresos:.2f}")
        print(f"Gastos Totales: ${gastos:.2f}")
        print(f"Capacidad de Ahorro: ${ahorro:.2f}")

    def guardar_datos(self):
        with open('datos_financieros.pkl', 'wb') as archivo:
            pickle.dump(self.transacciones, archivo)
        print("Datos guardados exitosamente.")

    def cargar_datos(self):
        try:
            with open('datos_financieros.pkl', 'rb') as archivo:
                self.transacciones = pickle.load(archivo)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos, iniciando con una lista de transacciones vacía.")

def mostrar_menu():
    print("\nGestor Financiero")
    print("1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Calcular Balance")
    print("4. Guardar Datos")
    print("5. Salir")

def ejecutar_aplicacion():
    gestor = GestorFinanciero()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            monto = float(input("Ingrese el monto: "))
            fecha = datetime.strptime(input("Ingrese la fecha (YYYY-MM-DD): "), '%Y-%m-%d')
            descripcion = input("Ingrese la descripción: ")
            tipo = input("Ingrese el tipo (Ingreso/Gasto): ")
            gestor.agregar_transaccion(monto, fecha, descripcion, tipo)
        elif opcion == '2':
            gestor.listar_transacciones()
        elif opcion == '3':
            gestor.calcular_balance()
        elif opcion == '4':
            gestor.guardar_datos()
        elif opcion == '5':
            gestor.guardar_datos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_aplicacion()
