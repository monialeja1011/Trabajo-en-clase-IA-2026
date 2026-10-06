"""
neurona_and.py

Implementación de una neurona artificial simple
para aprender la compuerta lógica AND.

Se utiliza Python puro para la neurona.
Matplotlib se utiliza únicamente para visualizar
la evolución del error.
"""

import matplotlib.pyplot as plt


# ============================================================
# 1. FUNCIÓN DE ACTIVACIÓN
# ============================================================

def escalon(z):
    """
    Función de activación escalón.

    Si z es mayor o igual a 0 devuelve 1.
    Si z es menor que 0 devuelve 0.
    """
    return 1 if z >= 0 else 0


# ============================================================
# 2. DEFINIR LA NEURONA
# ============================================================

def neurona(x1, x2, w1, w2, b):
    """
    Calcula la salida de la neurona.
    """
    z = w1 * x1 + w2 * x2 + b
    return escalon(z)


# ============================================================
# 3. DATOS DE ENTRENAMIENTO
#    COMPUERTA LÓGICA AND
# ============================================================

datos = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
]


# ============================================================
# 4. PARÁMETROS INICIALES
# ============================================================

# Valores recomendados por el profesor
# para observar el proceso de aprendizaje.

w1 = 0.1
w2 = 0.1
b = 0.0

tasa_aprendizaje = 0.1


# Lista para guardar el error de cada época
errores_por_epoca = []


# ============================================================
# 5. ENTRENAMIENTO
# ============================================================

print("=" * 60)
print("ENTRENAMIENTO DE UNA NEURONA PARA LA COMPUERTA AND")
print("=" * 60)

print(
    f"Parámetros iniciales: "
    f"w1={w1}, w2={w2}, b={b}\n"
)


for epoca in range(10):

    error_total = 0

    print(f"--- Época {epoca + 1} ---")

    for x1, x2, y_real in datos:

        # ----------------------------------------------------
        # Predicción
        # ----------------------------------------------------

        y_pred = neurona(
            x1,
            x2,
            w1,
            w2,
            b
        )

        # ----------------------------------------------------
        # Cálculo del error
        # ----------------------------------------------------

        error = y_real - y_pred

        error_total += abs(error)

        # ----------------------------------------------------
        # Ajuste de pesos y bias
        # ----------------------------------------------------

        w1 += tasa_aprendizaje * error * x1

        w2 += tasa_aprendizaje * error * x2

        b += tasa_aprendizaje * error

        # ----------------------------------------------------
        # Mostrar resultados
        # ----------------------------------------------------

        print(
            f" Entrada: ({x1}, {x2}) | "
            f"Real: {y_real} | "
            f"Pred: {y_pred} | "
            f"Error: {error}"
        )

    # --------------------------------------------------------
    # Guardar error de la época
    # --------------------------------------------------------

    errores_por_epoca.append(error_total)

    print(f" Error total: {error_total}")

    print(
        f" Parámetros actuales: "
        f"w1={w1:.3f}, "
        f"w2={w2:.3f}, "
        f"b={b:.3f}\n"
    )

    # --------------------------------------------------------
    # Verificar si la neurona ya aprendió
    # --------------------------------------------------------

    if error_total == 0:

        print(
            f"La neurona aprendió "
            f"en {epoca + 1} épocas.\n"
        )

        break


# ============================================================
# 6. PRUEBA FINAL
# ============================================================

print("=" * 60)
print("PRUEBA FINAL")
print("=" * 60)

for x1, x2, y_real in datos:

    y_pred = neurona(
        x1,
        x2,
        w1,
        w2,
        b
    )

    estado = "OK" if y_pred == y_real else "X"

    print(
        f" {estado} "
        f"Entrada: ({x1}, {x2}) | "
        f"Esperado: {y_real} | "
        f"Predicho: {y_pred}"
    )


# ============================================================
# 7. GRAFICAR LA EVOLUCIÓN DEL ERROR
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, len(errores_por_epoca) + 1),
    errores_por_epoca,
    marker="o"
)

plt.title(
    "Evolución del Error durante el Entrenamiento"
)

plt.xlabel("Época")

plt.ylabel("Error Total")

plt.grid(True)

plt.savefig(
    "data/evolucion_error.png",
    dpi=150
)

plt.close()

print()
print("Gráfico guardado: data/evolucion_error.png")