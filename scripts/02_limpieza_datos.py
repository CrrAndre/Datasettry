# =============================================================
# Script 02 - Limpieza y preparación de datos
# =============================================================
# Equivalente en Excel: corregir celdas vacías, eliminar
# duplicados, cambiar formatos de columnas
# =============================================================

import pandas as pd

# Cargar el dataset
df = pd.read_csv("datasets/ventas.csv")

print("=== Dataset original ===")
print(df.head())
print()

# --------------------------------------------------
# 1. Revisar valores nulos (celdas vacías)
# --------------------------------------------------
# En Excel ves las celdas vacías visualmente
# En Python usamos .isnull().sum()

print("=== Valores nulos por columna ===")
print(df.isnull().sum())
print()

# --------------------------------------------------
# 2. Convertir la columna 'fecha' a tipo fecha
# --------------------------------------------------
# En Excel: seleccionas la columna y cambias el formato a Fecha
# En Python: usamos pd.to_datetime()

df["fecha"] = pd.to_datetime(df["fecha"])
print("=== Tipo de 'fecha' después de la conversión ===")
print(df["fecha"].dtype)
print()

# --------------------------------------------------
# 3. Agregar columnas derivadas
# --------------------------------------------------
# En Excel: insertas una columna nueva con una fórmula
# En Python: df["nueva_columna"] = operación

# Agregar el mes como columna nueva
df["mes"] = df["fecha"].dt.month

# Agregar el nombre del mes
df["nombre_mes"] = df["fecha"].dt.month_name()

print("=== Dataset con columnas de mes agregadas ===")
print(df[["fecha", "mes", "nombre_mes", "total"]].head(10))
print()

# --------------------------------------------------
# 4. Verificar y eliminar duplicados
# --------------------------------------------------
# En Excel: Datos > Quitar duplicados
# En Python: .drop_duplicates()

duplicados = df.duplicated().sum()
print(f"=== Filas duplicadas encontradas: {duplicados} ===")

df_limpio = df.drop_duplicates()
print(f"Filas antes: {len(df)}  |  Filas después: {len(df_limpio)}")
print()

# --------------------------------------------------
# 5. Filtrar filas (como filtros de Excel)
# --------------------------------------------------
# En Excel: Datos > Filtro, seleccionas una categoría
# En Python: usamos condiciones entre corchetes

ventas_norte = df[df["region"] == "Norte"]
print("=== Ventas de la región Norte ===")
print(ventas_norte[["fecha", "vendedor", "producto", "total"]])
print()

ventas_electronica = df[df["categoria"] == "Electrónica"]
print("=== Ventas de categoría Electrónica ===")
print(ventas_electronica[["fecha", "vendedor", "producto", "total"]])
