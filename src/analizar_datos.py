import numpy as np

def analizar_datos(datos_numericos):
    if datos_numericos is None or len(datos_numericos) == 0:
        return None

    hectareas = datos_numericos[:, 0]
    produccion = datos_numericos[:, 1]

    estadisticas = {
        'hectareas': {
            'media': np.mean(hectareas),
            'mediana': np.median(hectareas),
            'desviacion': np.std(hectareas),
            'minimo': np.min(hectareas),
            'maximo': np.max(hectareas)
        },
        'produccion': {
            'media': np.mean(produccion),
            'mediana': np.median(produccion),
            'desviacion': np.std(produccion),
            'minimo': np.min(produccion),
            'maximo': np.max(produccion)
        }
    }

    return estadisticas
