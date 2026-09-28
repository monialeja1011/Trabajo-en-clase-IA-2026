import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_datos
from analizar_datos import analizar_datos

def generar_visualizaciones(datos_numericos, datos_completos):
    if datos_numericos is None or len(datos_numericos) == 0:
        return

    hectareas = datos_numericos[:, 0]
    produccion = datos_numericos[:, 1]
    nombres = [fila[0] for fila in datos_completos]

    # Gráfico de barras
    plt.figure(figsize=(10, 5))
    plt.bar(nombres, hectareas, color='skyblue')
    plt.title('Hectáreas por Cultivo')
    plt.xlabel('Cultivo')
    plt.ylabel('Hectáreas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('data/hectareas_por_cultivo.png')

    # Dispersión
    plt.figure(figsize=(8, 6))
    plt.scatter(hectareas, produccion, color='green', alpha=0.7)
    plt.title('Relación: Hectáreas vs Producción')
    plt.xlabel('Hectáreas')
    plt.ylabel('Producción (toneladas)')
    plt.grid(True)
    plt.savefig('data/hectareas_vs_produccion.png')

    # Histograma
    plt.figure(figsize=(8, 5))
    plt.hist(produccion, bins=5, color='orange', edgecolor='black')
    plt.title('Distribución de la Producción')
    plt.xlabel('Producción (toneladas)')
    plt.ylabel('Frecuencia')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.savefig('data/distribucion_produccion.png')

def main():
    datos_numericos, datos_completos, columnas = cargar_datos('data/cultivos_detalle.csv')

    if datos_numericos is None:
        return

    estadisticas = analizar_datos(datos_numericos)
    print("Estadísticas:", estadisticas)

    generar_visualizaciones(datos_numericos, datos_completos)

if __name__ == "__main__":
    main()
