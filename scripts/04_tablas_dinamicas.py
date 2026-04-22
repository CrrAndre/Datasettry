# =============================================================
# Script 04 - Tablas dinámicas con pandas (pivot tables)
# =============================================================
# Equivalente en Excel: Insertar > Tabla dinámica
# pandas tiene una función llamada pivot_table() que hace
# exactamente lo mismo que las tablas dinámicas de Excel
# =============================================================

import pandas as pd

# Cargar el dataset y preparar la columna de fecha
df = pd.read_csv("datasets/ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

# --------------------------------------------------
# Tabla dinámica 1: Total de ventas por vendedor y región
# --------------------------------------------------
# Excel: Filas = vendedor, Columnas = región, Valores = suma de total

print("=== Tabla dinámica: Total de ventas por vendedor y región ===")
tabla1 = pd.pivot_table(
    df,
    values="total",       # Columna que queremos calcular (Valores en Excel)
    index="vendedor",     # Filas de la tabla dinámica
    columns="region",     # Columnas de la tabla dinámica
    aggfunc="sum",        # Operación: suma (como SUMA en Excel)
    fill_value=0,         # Rellenar celdas vacías con 0
    margins=True,         # Agregar fila/columna de totales (como "Gran total")
    margins_name="TOTAL", # Nombre de la fila/columna de totales
)
print(tabla1.to_string())
print()

# --------------------------------------------------
# Tabla dinámica 2: Cantidad vendida por producto y mes
# --------------------------------------------------
print("=== Tabla dinámica: Cantidad vendida por producto y mes ===")
tabla2 = pd.pivot_table(
    df,
    values="cantidad",
    index="producto",
    columns="mes",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="TOTAL",
)
# Renombrar columnas de mes para que sean más legibles
tabla2.columns = [
    f"Mes {c}" if c != "TOTAL" else "TOTAL" for c in tabla2.columns
]
print(tabla2.to_string())
print()

# --------------------------------------------------
# Tabla dinámica 3: Promedio de venta por categoría y región
# --------------------------------------------------
print("=== Tabla dinámica: Promedio de venta por categoría y región ===")
tabla3 = pd.pivot_table(
    df,
    values="total",
    index="categoria",
    columns="region",
    aggfunc="mean",       # Promedio (como PROMEDIO en Excel)
    fill_value=0,
)
print(tabla3.round(0).to_string())
print()

# --------------------------------------------------
# Tabla dinámica 4: Múltiples métricas a la vez
# --------------------------------------------------
# En Excel puedes agregar varios campos de valor en una tabla dinámica
# En pandas puedes pasar una lista de funciones a aggfunc

print("=== Tabla dinámica: Resumen de ventas por vendedor ===")
tabla4 = pd.pivot_table(
    df,
    values="total",
    index="vendedor",
    aggfunc=["sum", "mean", "count"],  # Suma, promedio y conteo
)
tabla4.columns = ["Total ventas", "Venta promedio", "Num. transacciones"]
print(tabla4.round(0).to_string())
print()

# --------------------------------------------------
# Exportar una tabla dinámica a Excel
# --------------------------------------------------
# En Excel ya estás en Excel, pero en Python puedes exportar
# el resultado de vuelta a un archivo .xlsx

tabla1.to_excel("datasets/tabla_dinamica_ventas.xlsx")
print("✅ Tabla dinámica exportada a: datasets/tabla_dinamica_ventas.xlsx")
