import pickle

def verificar_datos():
    try:
        with open('datos_financieros.pkl', 'rb') as archivo:
            transacciones = pickle.load(archivo)
            for transaccion in transacciones:
                print(transaccion)
    except FileNotFoundError:
        print("El archivo 'datos_financieros.pkl' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    verificar_datos()
