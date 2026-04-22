# =============================================================
# Script 01 - Leer y explorar datos con pandas
# =============================================================
# Equivalente en Excel: abrir un archivo CSV y ver su contenido
# =============================================================

import pandas as pd

# --------------------------------------------------
# 1. Cargar el archivo CSV
# --------------------------------------------------
# En Excel harías: Archivo > Abrir > ventas.csv
# En Python usamos pd.read_csv()

df = pd.read_csv("datasets/ventas.csv")

# --------------------------------------------------
# 2. Ver las primeras filas del dataset
# --------------------------------------------------
# En Excel: simplemente ves las primeras filas de la hoja
# En Python: .head() muestra las primeras 5 filas por defecto

print("=== Primeras 5 filas ===")
print(df.head())
print()

# --------------------------------------------------
# 3. Ver el tamaño del dataset
# --------------------------------------------------
# .shape devuelve (número de filas, número de columnas)

filas, columnas = df.shape
print(f"=== Tamaño del dataset ===")
print(f"Filas: {filas}   |   Columnas: {columnas}")
print()

# --------------------------------------------------
# 4. Ver los nombres de las columnas
# --------------------------------------------------
print("=== Nombres de columnas ===")
print(df.columns.tolist())
print()

# --------------------------------------------------
# 5. Ver los tipos de datos de cada columna
# --------------------------------------------------
# En Excel no ves esto directamente, pero es importante en Python

print("=== Tipos de datos ===")
print(df.dtypes)
print()

# --------------------------------------------------
# 6. Ver un resumen estadístico rápido
# --------------------------------------------------
# En Excel usarías funciones como PROMEDIO(), MIN(), MAX()
# En Python: .describe() hace todo eso de una vez

print("=== Resumen estadístico ===")
print(df.describe())
print()

# --------------------------------------------------
# 7. Ver valores únicos de una columna
# --------------------------------------------------
# Útil para conocer las categorías disponibles

print("=== Vendedores únicos ===")
print(df["vendedor"].unique())

print("\n=== Regiones únicas ===")
print(df["region"].unique())
