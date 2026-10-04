import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# PREPARACIÓN DE DATOS PARA MACHINE LEARNING - CAFÉ


print("=" * 60)
print("PREPARACIÓN DE DATOS PARA MACHINE LEARNING - CAFÉ")
print("=" * 60)



# 1. CARGAR DATOS

def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    print(f"Datos cargados correctamente: {df.shape[0]} filas, {df.shape[1]} columnas.")
    return df

# 2. EXPLORACIÓN DE DATOS


def explorar_datos(df):
    print("\n" + "=" * 60)
    print("PRIMERAS 5 FILAS")
    print("=" * 60)
    print(df.head())

    print("\n" + "=" * 60)
    print("INFORMACIÓN GENERAL")
    print("=" * 60)
    df.info()

    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 60)
    print(df.describe())

    print("\n" + "=" * 60)
    print("VALORES NULOS POR COLUMNA")
    print("=" * 60)
    print(df.isnull().sum())

# 3. LIMPIEZA Y PREPARACIÓN DE DATOS

def limpiar_datos(df):

    print("\n" + "=" * 60)
    print("LIMPIEZA DE DATOS")
    print("=" * 60)

    # Mostrar cantidad de valores nulos
    nulos = df.isnull().sum()

    if nulos.sum() == 0:
        print("No se encontraron valores nulos.")
    else:
        print("Valores nulos encontrados:")
        print(nulos[nulos > 0])

        # Rellenar valores numéricos con la mediana
        columnas_numericas = df.select_dtypes(include=np.number).columns

        for columna in columnas_numericas:
            if df[columna].isnull().sum() > 0:
                mediana = df[columna].median()
                df[columna] = df[columna].fillna(mediana)
                print(
                    f"Valores nulos en '{columna}' "
                    f"reemplazados con la mediana: {mediana}"
                )

    # Crear columna derivada
    df["porcentaje_cosecha"] = (
        df["hectareas_cosechadas"] /
        df["hectareas_sembradas"]
    ) * 100

    print("\nColumna 'porcentaje_cosecha' creada.")

    return df

# 4. CODIFICACIÓN DE VARIABLES CATEGÓRICAS

def preparar_ml(df):

    print("\n" + "=" * 60)
    print("PREPARACIÓN PARA MACHINE LEARNING")
    print("=" * 60)

    # El código del municipio es un identificador,
    # por lo tanto no se utiliza como variable numérica.
    df_ml = df.drop(columns=["codigo_municipio"])

    # One-Hot Encoding para la variable categórica municipio
    df_ml = pd.get_dummies(
        df_ml,
        columns=["municipio"],
        prefix="municipio",
        dtype=int
    )

    print("Codificación One-Hot aplicada a 'municipio'.")

    print("\nCOLUMNAS DEL DATASET PREPARADO:")
    print(df_ml.columns.tolist())

    print("\nPRIMERAS 5 FILAS:")
    print(df_ml.head())

    return df_ml

# 5. VISUALIZACIÓN DE DATOS

def visualizar_datos(df):

    print("\n" + "=" * 60)
    print("GENERANDO VISUALIZACIONES")
    print("=" * 60)


    sns.set_theme(style="whitegrid")

    
    # Gráfico 1: Distribución de la producción

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="produccion",
        kde=True
    )

    plt.title("Distribución de la Producción de Café")
    plt.xlabel("Producción")
    plt.ylabel("Frecuencia")
    plt.tight_layout()

    plt.savefig(
        "clase8/data/distribucion_produccion_cafe.png",
        dpi=150
    )

    plt.close()

    print("Gráfico 1 guardado: distribucion_produccion_cafe.png")

    
    # Gráfico 2: Producción promedio por municipio

    plt.figure(figsize=(12, 8))

    produccion_municipio = (
        df.groupby("municipio")["produccion"]
        .mean()
        .sort_values(ascending=False)
    )

    sns.barplot(
        x=produccion_municipio.values,
        y=produccion_municipio.index
    )

    plt.title("Producción Promedio de Café por Municipio")
    plt.xlabel("Producción Promedio")
    plt.ylabel("Municipio")
    plt.tight_layout()

    plt.savefig(
        "clase8/data/produccion_por_municipio.png",
        dpi=150
    )

    plt.close()

    print("Gráfico 2 guardado: produccion_por_municipio.png")

    
    # Gráfico 3: Hectáreas cosechadas vs producción

    plt.figure(figsize=(10, 6))

    sns.regplot(
        data=df,
        x="hectareas_cosechadas",
        y="produccion",
        scatter_kws={"alpha": 0.6}
    )

    plt.title("Relación entre Hectáreas Cosechadas y Producción")
    plt.xlabel("Hectáreas Cosechadas")
    plt.ylabel("Producción")
    plt.tight_layout()

    plt.savefig(
        "clase8/data/hectareas_vs_produccion_cafe.png",
        dpi=150
    )

    plt.close()

    print("Gráfico 3 guardado: hectareas_vs_produccion_cafe.png")

# 6. EJECUCIÓN DEL PROCESO COMPLETO

if __name__ == "__main__":

    # Cargar dataset
    df = cargar_datos("clase8/data/cafe_valle_limpio.csv")

    # Explorar dataset
    explorar_datos(df)

    # Limpiar y crear columna derivada
    df = limpiar_datos(df)

    # Generar visualizaciones
    visualizar_datos(df)

    # Preparar datos para Machine Learning
    df_ml = preparar_ml(df)

    # Guardar dataset preparado
    ruta_salida = "clase8/data/cafe_preparado_ml.csv"

    df_ml.to_csv(ruta_salida, index=False)

    print("\n" + "=" * 60)
    print("DATASET PREPARADO GUARDADO")
    print("=" * 60)
    print(f"Archivo: {ruta_salida}")
    print(f"Filas: {df_ml.shape[0]}")
    print(f"Columnas: {df_ml.shape[1]}")

    print("\nProceso completado exitosamente.")