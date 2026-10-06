# Clase 8 – Implementación de una Neurona Artificial
## COTECNOVA – Inteligencia Artificial 2026

* **Docente:** Jhon James Cano Sánchez
* **Estudiante:** Mónica Alejandra Parra
* **Programa:** Ingeniería de Sistemas
* **Actividad:** Implementación de neuronas artificiales para compuertas lógicas

---

## 1. Descripción

En esta actividad se implementan **neuronas artificiales sencillas** utilizando Python. El objetivo principal es comprender de manera práctica cómo funciona una neurona artificial: cómo recibe entradas, realiza operaciones matemáticas, genera predicciones y ajusta sus parámetros durante el entrenamiento para disminuir el error.

Como parte de la actividad se implementaron las siguientes compuertas lógicas:
* **AND** (Ejercicio principal trabajado durante la clase)
* **OR** (Actividad complementaria)
* **NOT** (Actividad complementaria)

También se utiliza **Matplotlib** para visualizar la evolución del error durante el entrenamiento. El proyecto se ejecuta utilizando **Docker**, **WSL Ubuntu** y **Visual Studio Code**.

---

## 2. Objetivos

### Objetivo general
Implementar y entrenar neuronas artificiales sencillas en Python para aprender diferentes compuertas lógicas.

### Objetivos específicos
* **Comprender** el funcionamiento básico de una neurona artificial.
* **Implementar** una función de activación tipo escalón.
* **Trabajar** con pesos, sesgo y tasa de aprendizaje.
* **Entrenar** una neurona utilizando ejemplos de compuertas lógicas (AND, OR, NOT).
* **Observar** la disminución del error y generar gráficas de su evolución.
* **Comprender** las limitaciones de un perceptrón simple.
* **Ejecutar** el proyecto dentro de un entorno Docker.

---

## 3. Compuertas lógicas implementadas

Durante la actividad se trabajaron tres compuertas lógicas: **AND, OR y NOT**.

### 3.1. Compuerta AND
La compuerta AND devuelve `1` únicamente cuando **ambas entradas son 1**.

| Entrada 1 | Entrada 2 | Salida esperada |
| :-------: | :-------: | :-------------: |
|     0     |     0     |        0        |
|     0     |     1     |        0        |
|     1     |     0     |        0        |
|     1     |     1     |        1        |

### 3.2. Compuerta OR
La compuerta OR devuelve `1` cuando **al menos una de las entradas es 1**.

| Entrada 1 | Entrada 2 | Salida esperada |
| :-------: | :-------: | :-------------: |
|     0     |     0     |        0        |
|     0     |     1     |        1        |
|     1     |     0     |        1        |
|     1     |     1     |        1        |

### 3.3. Compuerta NOT
La compuerta NOT devuelve el valor contrario de su entrada. Para reutilizar la misma estructura de entrenamiento utilizada para AND y OR, en la implementación de NOT se utilizó una segunda entrada con valor `0`.

| Entrada | Entrada Auxiliar | Salida esperada |
| :-----: | :--------------: | :-------------: |
|    0    |        0         |        1        |
|    1    |        0         |        0        |



---

## 4. Funcionamiento de la neurona

La neurona recibe entradas que se combinan con diferentes pesos. Para las compuertas AND y OR se utilizan dos entradas (`x1`, `x2`), cada una con un peso asociado (`w1`, `w2`) y un sesgo (`b`).

### Cálculo de la suma ponderada
```text
z = w1*x1 + w2*x2 + b
```

### Función de activación tipo escalón
```python
def escalon(z):
    return 1 if z >= 0 else 0
```
La función escalón permite convertir el resultado de la suma ponderada en una salida binaria: si `z >= 0` la salida es `1`, de lo contrario es `0`.

---

## 5. Parámetros de entrenamiento

Los valores iniciales utilizados fueron:
```python
w1 = 0.1
w2 = 0.1
b = 0.0
tasa_aprendizaje = 0.1
```
La **tasa de aprendizaje** determina qué tan grandes son los cambios realizados en los pesos y el sesgo durante el entrenamiento.

---

## 6. Entrenamiento de las neuronas

Durante el entrenamiento, la neurona recibe los datos de entrada, genera una predicción y la compara con el valor esperado.

### Cálculo del error
```text
error = y_real - y_pred
```

### Actualización de parámetros
```text
w1 = w1 + tasa_aprendizaje * error * x1
w2 = w2 + tasa_aprendizaje * error * x2
b  = b  + tasa_aprendizaje * error
```
Este proceso se repite durante diferentes épocas hasta que la neurona consigue clasificar correctamente los ejemplos de entrenamiento.

---

## 7. Implementación de la actividad

El proyecto se estructuró de la siguiente manera dentro del entorno de desarrollo:

* **Actividad de clase (Compuerta AND):** Implementada en el archivo `src/neurona_and.py`.
* **Actividad complementaria (Compuertas OR y NOT):** Implementadas en el archivo `src/neuronas_logicas.py`.

Ambos archivos contienen la lógica de inicialización de parámetros, entrenamiento, cálculo de errores, actualización de pesos/bias, verificación de predicciones y exportación de métricas.

---

## 8. Resultados del entrenamiento y Convergencia

### 8.1. Resumen de resultados

| Compuerta | Épocas utilizadas | Resultado Final |
| :-------- | :---------------: | :-------------- |
| **AND**   |       **3**       | Aprendió correctamente tras llegar a error 0 en la 3ª época. |
| **OR**    |       **2**       | Aprendió correctamente tras llegar a error 0 en la 2ª época. |
| **NOT**   |       **4**       | Aprendió correctamente tras llegar a error 0 en la 4ª época. |

### 8.2. Predicciones finales obtenidas

* **AND:** `(0,0) → 0`, `(0,1) → 0`, `(1,0) → 0`, `(1,1) → 1`
* **OR:** `(0,0) → 0`, `(0,1) → 1`, `(1,0) → 1`, `(1,1) → 1`
* **NOT:** `0 → 1`, `1 → 0`

---

## 9. Visualización del error

Durante el entrenamiento se almacena el error total por época en una lista (`errores_por_epoca = []`) para posteriormente generar y guardar las gráficas utilizando **Matplotlib** en las siguientes rutas:
* `data/evolucion_error.png` (AND)
* `data/error_or.png`
* `data/error_not.png`

---

## 10. Visualización del error

Durante el entrenamiento se almacena el error total por época para monitorear el progreso del aprendizaje:

```python
errores_por_epoca = []
```

Posteriormente se generan gráficas utilizando **Matplotlib** vinculando:
* **Eje X:** Número de época.
* **Eje Y:** Error total.

Las gráficas generadas y almacenadas automáticamente son:
* `data/evolucion_error.png` (Compuerta AND)
* `data/error_or.png` (Compuerta OR)
* `data/error_not.png` (Compuerta NOT)

Estas gráficas permiten observar visualmente la velocidad de convergencia y el descenso del error durante el aprendizaje de cada compuerta.

---

## 11. Reflexión sobre el aprendizaje

### ¿Cuántas épocas necesitó cada compuerta?

Los resultados medidos en la ejecución actual fueron:

| Compuerta | Épocas Requeridas |
| :--- | :---: |
| **AND** | 3 |
| **OR** | 2 |
| **NOT** | 4 |

La compuerta **OR** necesitó menos épocas en esta ejecución, mientras que **NOT** requirió la mayor cantidad. Esto no significa que una compuerta sea inherentemente más compleja que otra; el número de épocas depende directamente de la inicialización de los parámetros aleatorios y del orden de los datos presentados.

### ¿Fue necesario ajustar la tasa de aprendizaje?

**No fue necesario** modificar el hiperparámetro inicial. Se utilizó una tasa fija:

```python
tasa_aprendizaje = 0.1
```

Con este valor las tres compuertas lograron converger con éxito. La tasa de aprendizaje (\(\alpha\)) controla el impacto de las correcciones en el entrenamiento:
* **Muy pequeña:** El aprendizaje se vuelve excesivamente lento.
* **Muy grande:** Los cambios son drásticos y el entrenamiento se vuelve inestable o divergente.
* **Valor adecuado (0.1):** Permite realizar ajustes progresivos y estables.

### ¿Qué diferencias se encontraron entre AND y OR?

Ambas compuertas representan problemas **linealmente separables**, lo que significa que sus clases pueden dividirse perfectamente mediante una línea recta en un plano bidimensional.

* **AND:** Devuelve `1` únicamente cuando ambas entradas son simultáneamente `1`.
* **OR:** Devuelve `1` cuando al menos una de las entradas es `1`.

En esta ejecución, AND requirió **3 épocas** y OR requirió **2 épocas**. Ambas fueron resueltas por una sola neurona artificial gracias a su naturaleza lineal.

### ¿Por qué la compuerta XOR no puede ser aprendida por una sola neurona?

La tabla de verdad de la compuerta **XOR (OR Exclusiva)** es la siguiente:

| Entrada 1 | Entrada 2 | Salida Esperada |
| :-------: | :-------: | :-------------: |
|     0     |     0     |        0        |
|     0     |     1     |        1        |
|     1     |     0     |        1        |
|     1     |     1     |        0        |

Los estados de salida de XOR **no pueden separarse mediante una sola línea recta** en el plano. Al no ser linealmente separable, un perceptrón simple o neurona única falla al intentar resolverlo. Para solucionar el problema de la compuerta XOR se requiere una estructura jerárquica más avanzada, como una **Red Neuronal Multicapa (MLP)**.

---

## 12. Estructura del proyecto

El espacio de trabajo quedó organizado con la siguiente jerarquía de archivos y directorios:

```text
clase8/
│
├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── data/
│   ├── evolucion_error.png
│   ├── error_or.png
│   └── error_not.png
│
└── src/
    ├── neurona_and.py
    └── neuronas_logicas.py
```

---

## 13. Configuración del entorno

La infraestructura local para el desarrollo de la práctica está compuesta por:
* **Sistema Operativo:** Windows con subsistema **WSL Ubuntu**.
* **Virtualización:** **Docker** y **Docker Compose**.
* **IDE:** **Visual Studio Code**.
* **Entorno de Ejecución:** **Python 3.12** complementado con las librerías **NumPy** y **Matplotlib**.

---

## 14. Docker

El entorno se empaqueta en un contenedor controlado para garantizar la reproducibilidad:
* **Nombre del contenedor:** `python_ia`
* **Punto de montaje (Volumen):** `/app`

El archivo `docker-compose.yml` gestiona la construcción automática del entorno aislado, evitando conflictos de dependencias en el sistema anfitrión.

---

## 15. Dependencias

El archivo `requirements.txt` especifica las librerías necesarias:

```text
numpy
matplotlib
```

### Comandos de administración del contenedor:

* **Reconstruir la imagen sin caché (tras modificar dependencias):**
  ```bash
  docker compose build --no-cache
  ```
* **Iniciar el contenedor en segundo plano (detached):**
  ```bash
  docker compose up -d
  ```

---

## 16. Ejecución del proyecto

Para ejecutar los scripts de forma secuencial dentro del contenedor, se siguen estos pasos en la terminal:

```bash
# 1. Ingresar al directorio del proyecto en WSL
cd ~/ia-python/clase8

# 2. Iniciar los servicios de Docker
docker compose up -d

# 3. Acceder a la terminal interactiva del contenedor
docker exec -it python_ia bash

# 4. Ejecutar el ejercicio principal (Compuerta AND)
python src/neurona_and.py

# 5. Ejecutar la actividad complementaria (Compuertas OR y NOT)
python src/neuronas_logicas.py
```

---

## 17. Verificación de resultados

Una vez finalizadas las ejecuciones, se valida la correcta generación de los archivos de salida:

```bash
ls -l data
```

**Artefactos verificados en `/data`:**
* `data/evolucion_error.png`
* `data/error_or.png`
* `data/error_not.png`

---

## 18. Subida a GitHub

Control de versiones y despliegue del código mediante Git:

```bash
# Verificar los archivos modificados
git status

# Añadir todos los cambios al área de preparación (staging)
git add .

# Crear un commit descriptivo
git commit -m "Implementar neuronas para compuertas AND OR y NOT"

# Sincronizar cambios con el repositorio remoto
git push
```

---

## 19. Cierre y Resumen de la actividad

Esta práctica permitió asimilar los componentes clave del ciclo de vida de una neurona artificial desde cero:
1. **Recepción de Entradas (`x`) y Pesos (`w`):** Simulación de los canales sinápticos.
2. **Suma Ponderada + Bias (`z`):** Integración de señales de entrada con el umbral de activación.
3. **Predicción (`y_pred`):** Mapeo de la señal resultante mediante una función escalón binaria.
4. **Cálculo de Error y Retroalimentación:** Medición de la desviación frente a la salida real para aplicar la regla del perceptrón de forma iterativa hasta alcanzar un error global de cero.

---

## 20. Conexión con Inteligencia Artificial

A pesar de la simplicidad de las compuertas lógicas, modelar estos flujos sienta los cimientos de los algoritmos modernos de Machine Learning. Comprender la interacción entre variables como el *Bias*, la *Tasa de Aprendizaje* y los *Pesos Sinápticos* facilita el salto hacia arquitecturas complejas y herramientas profesionales de la industria como **Scikit-Learn**, **TensorFlow** o **PyTorch**.

---

## 21. Próxima clase

Tomando como referencia la guía de la asignatura, los siguientes objetivos temáticos consisten en:
* Implementación completa de un perceptrón utilizando **Descenso del Gradiente** en Python puro.
* Entrenamiento del modelo empleando un **Dataset real**.
* Visualización matemática de la **Frontera de decisión**.
* Comparación de rendimiento contra las neuronas lógicas desarrolladas en esta sesión.

---

## 22. Anexo – Cheat Sheet de la Neurona Artificial

| Concepto | Fórmula / Código | Descripción |
| :--- | :--- | :--- |
| **Suma ponderada** | `z = w1*x1 + w2*x2 + b` | Combina las entradas multiplicadas por sus pesos y suma el sesgo. |
| **Función escalón** | `1 if z >= 0 else 0` | Mapea el valor de entrada a una salida binaria discreta. |
| **Predicción** | `y_pred = escalon(z)` | El resultado binario final computado por la neurona. |
| **Error** | `error = y_real - y_pred` | Magnitud y dirección de la desviación en la predicción. |
| **Ajuste de peso** | `w += α * error * x` | Corrección aplicada a las conexiones sinápticas. |
| **Ajuste de bias** | `b += α * error` | Modificación del umbral de disparo intrínseco. |
| **Tasa de aprendizaje** | `α` u `eta` | Escala la magnitud del paso de actualización para evitar inestabilidad. |

---

## 23. Conclusión final

La actividad cumplió satisfactoriamente con el diseño e implementación de una neurona artificial desde cero, demostrando su efectividad en problemas linealmente separables (**AND, OR y NOT**) con una convergencia rápida entre **2 y 4 épocas** bajo una tasa de aprendizaje estable de **0.1**. La monitorización del error mediante Matplotlib sirvió para corroborar empíricamente la efectividad matemática de las reglas de actualización. Finalmente, el análisis teórico de la compuerta **XOR** delimitó las fronteras del perceptrón simple, abriendo de manera orgánica el camino hacia el estudio avanzado de las Redes Neuronales Artificiales.
