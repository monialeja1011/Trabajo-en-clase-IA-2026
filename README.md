Proyecto IA – Análisis Exploratorio de Datos con Docker y NumPy
Este proyecto corresponde a la asignatura Inteligencia Artificial.
El objetivo es construir un entorno reproducible usando WSL, Docker y Python,
y realizar un Análisis Exploratorio de Datos (EDA) sobre un dataset de cultivos.

Tecnologías utilizadas
Python 3.12 (dentro de Docker)

NumPy

Matplotlib

Docker Desktop

WSL 2 (Ubuntu)

VSCode

Git y GitHub

Cómo ejecutar el proyecto
Construir la imagen:
docker compose build

Levantar el contenedor:
docker compose up -d

Entrar al contenedor:
docker exec -it ia_python bash

Ejecutar el EDA:
python src/eda_cultivos.py

Las gráficas se guardan en la carpeta data/.

Resultados generados
El script produce los siguientes archivos:

hectareas_por_cultivo.png

hectareas_vs_produccion.png

distribucion_produccion.png

Estructura del proyecto
ia-python/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
├── .dockerignore
│
├── src/
│   ├── main.py
│   ├── cargar_datos.py
│   ├── analizar_datos.py
│   └── eda_cultivos.py
│
├── data/
│   ├── cultivos_detalle.csv
│   ├── hectareas_por_cultivo.png
│   ├── hectareas_vs_produccion.png
│   └── distribucion_produccion.png
│
├── notebooks/
└── tests/
