import matplotlib.pyplot as plt


def escalon(z):
    """Función de activación tipo escalón."""
    return 1 if z >= 0 else 0


def entrenar_neurona(datos, epocas_maximas=10, tasa_aprendizaje=0.1):
    """
    Entrena una neurona utilizando la regla de actualización
    del perceptrón.

    Retorna:
        w1, w2, b, errores_por_epoca
    """

    w1 = 0.1
    w2 = 0.1
    b = 0.0

    errores_por_epoca = []

    for epoca in range(epocas_maximas):
        error_total = 0

        for x1, x2, esperado in datos:

            z = w1 * x1 + w2 * x2 + b
            predicho = escalon(z)

            error = esperado - predicho

            if error != 0:
                w1 = w1 + tasa_aprendizaje * error * x1
                w2 = w2 + tasa_aprendizaje * error * x2
                b = b + tasa_aprendizaje * error

            error_total += abs(error)

        errores_por_epoca.append(error_total)

        print(
            f"Época {epoca + 1}: "
            f"Error total = {error_total}"
        )

        print(
            f"  w1={w1:.3f}, "
            f"w2={w2:.3f}, "
            f"b={b:.3f}"
        )

        if error_total == 0:
            break

    return w1, w2, b, errores_por_epoca


def probar_neurona(datos, w1, w2, b):
    """Muestra las predicciones finales de la neurona."""

    resultados_correctos = True

    for x1, x2, esperado in datos:

        z = w1 * x1 + w2 * x2 + b
        predicho = escalon(z)

        estado = "OK" if predicho == esperado else "ERROR"

        print(
            f"{estado} Entrada: ({x1}, {x2}) | "
            f"Esperado: {esperado} | "
            f"Predicho: {predicho}"
        )

        if predicho != esperado:
            resultados_correctos = False

    return resultados_correctos


# COMPUERTA OR

print()
print("=" * 60)
print("ENTRENAMIENTO DE LA COMPUERTA OR")
print("=" * 60)

datos_or = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1)
]

w1_or, w2_or, b_or, errores_or = entrenar_neurona(
    datos_or,
    epocas_maximas=10,
    tasa_aprendizaje=0.1
)

print()
print("PRUEBA FINAL - OR")
print("-" * 60)

or_aprendio = probar_neurona(
    datos_or,
    w1_or,
    w2_or,
    b_or
)

print()
if or_aprendio:
    print("La neurona aprendió correctamente la compuerta OR.")
else:
    print("La neurona NO aprendió correctamente la compuerta OR.")


plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(errores_or) + 1),
    errores_or,
    marker="o"
)
plt.title("Evolución del Error - Compuerta OR")
plt.xlabel("Época")
plt.ylabel("Error Total")
plt.grid(True)
plt.savefig("data/error_or.png", dpi=150)
plt.close()

print("Gráfico guardado: data/error_or.png")


# COMPUERTA NOT

print()
print("=" * 60)
print("ENTRENAMIENTO DE LA COMPUERTA NOT")
print("=" * 60)

# Para NOT solo necesitamos una entrada.
# Se utiliza x2 = 0 para mantener la misma estructura.

datos_not = [
    (0, 0, 1),
    (1, 0, 0)
]

w1_not, w2_not, b_not, errores_not = entrenar_neurona(
    datos_not,
    epocas_maximas=10,
    tasa_aprendizaje=0.1
)

print()
print("PRUEBA FINAL - NOT")
print("-" * 60)

not_aprendio = probar_neurona(
    datos_not,
    w1_not,
    w2_not,
    b_not
)

print()
if not_aprendio:
    print("La neurona aprendió correctamente la compuerta NOT.")
else:
    print("La neurona NO aprendió correctamente la compuerta NOT.")


plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(errores_not) + 1),
    errores_not,
    marker="o"
)
plt.title("Evolución del Error - Compuerta NOT")
plt.xlabel("Época")
plt.ylabel("Error Total")
plt.grid(True)
plt.savefig("data/error_not.png", dpi=150)
plt.close()

print("Gráfico guardado: data/error_not.png")


# RESUMEN

print()
print("=" * 60)
print("RESUMEN DE RESULTADOS")
print("=" * 60)

print(f"OR  → {len(errores_or)} épocas")
print(f"NOT → {len(errores_not)} épocas")

print()
print("Archivos generados:")
print(" - data/error_or.png")
print(" - data/error_not.png")
