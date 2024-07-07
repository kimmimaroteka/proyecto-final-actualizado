import pickle
from datetime import datetime, timedelta
import random

# Generar datos ficticios
def generar_datos_ficticios():
    tipos = ['Ingreso', 'Gasto']
    transacciones = []

    for i in range(50):  # Generar 50 transacciones ficticias
        monto = round(random.uniform(10, 1000), 2)
        fecha = datetime.now() - timedelta(days=random.randint(0, 365))
        descripcion = f"Transacción {i+1}"
        tipo = random.choice(tipos)
        transaccion = {
            'monto': monto,
            'fecha': fecha,
            'descripcion': descripcion,
            'tipo': tipo
        }
        transacciones.append(transaccion)

    with open('datos_financieros.pkl', 'wb') as archivo:
        pickle.dump(transacciones, archivo)

    print("Datos ficticios generados y guardados en 'datos_financieros.pkl'.")

if __name__ == "__main__":
    generar_datos_ficticios()
