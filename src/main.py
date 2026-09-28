from cargar_datos import cargar_datos
from analizar_datos import analizar_datos
from eda_cultivos import generar_visualizaciones

def main():
    print("=" * 50)
    print(" ANÁLISIS EXPLORATORIO DE DATOS (EDA) - CULTIVOS")
    print("=" * 50)

    datos_numericos, datos_completos, columnas = cargar_datos('data/cultivos_detalle.csv')

    if datos_numericos is None:
        print("No se pudieron cargar los datos.")
        return

    estadisticas = analizar_datos(datos_numericos)
    print("\nEstadísticas calculadas:")
    print(estadisticas)

    print("\nGenerando visualizaciones...")
    generar_visualizaciones(datos_numericos, datos_completos)

    print("\nProceso completado. Gráficas guardadas en la carpeta data/.")

if __name__ == "__main__":
    main()

