import numpy as np
import csv

def cargar_datos(archivo_csv):
    datos = []
    nombres_columnas = []

    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            nombres_columnas = next(lector)

            for fila in lector:
                hectareas = float(fila[1])
                produccion = float(fila[2])
                datos.append([fila[0], hectareas, produccion, fila[3], fila[4]])

        print(f"Datos cargados correctamente: {len(datos)} registros.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no existe.")
        return None, None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None, None

    datos_numericos = np.array([[fila[1], fila[2]] for fila in datos], dtype=float)

    return datos_numericos, datos, nombres_columnas
