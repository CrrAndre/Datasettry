# =============================================================
# Script 03 - Análisis básico de datos
# =============================================================
# Equivalente en Excel: usar funciones como SUMA, PROMEDIO,
# CONTAR, MÁXIMO, MÍNIMO y agrupar por categorías
# =============================================================

import pandas as pd

# Cargar el dataset y preparar la columna de fecha
df = pd.read_csv("datasets/ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

# --------------------------------------------------
# 1. Estadísticas básicas de la columna 'total'
# --------------------------------------------------
# Equivalente Excel: funciones SUMA, PROMEDIO, MIN, MAX

print("=== Estadísticas de ventas (columna 'total') ===")
print(f"  Suma total:    ${df['total'].sum():,.0f}")
print(f"  Promedio:      ${df['total'].mean():,.0f}")
print(f"  Venta mínima:  ${df['total'].min():,.0f}")
print(f"  Venta máxima:  ${df['total'].max():,.0f}")
print(f"  Número de ventas: {len(df)}")
print()

# --------------------------------------------------
# 2. Total de ventas por vendedor
# --------------------------------------------------
# En Excel: usarías SUMAR.SI o una tabla dinámica
# En Python: .groupby() + .sum()

print("=== Total de ventas por vendedor ===")
por_vendedor = df.groupby("vendedor")["total"].sum().sort_values(ascending=False)
print(por_vendedor.to_string())
print()

# --------------------------------------------------
# 3. Total de ventas por región
# --------------------------------------------------
print("=== Total de ventas por región ===")
por_region = df.groupby("region")["total"].sum().sort_values(ascending=False)
print(por_region.to_string())
print()

# --------------------------------------------------
# 4. Total de ventas por categoría de producto
# --------------------------------------------------
print("=== Total de ventas por categoría ===")
por_categoria = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
print(por_categoria.to_string())
print()

# --------------------------------------------------
# 5. Número de ventas y total por mes
# --------------------------------------------------
# En Excel: usarías la función MES() y una tabla dinámica

print("=== Ventas por mes ===")
por_mes = df.groupby("mes").agg(
    num_ventas=("total", "count"),
    total_ventas=("total", "sum"),
    promedio_venta=("total", "mean"),
).round(0)
print(por_mes.to_string())
print()

# --------------------------------------------------
# 6. Top 3 productos más vendidos (por cantidad)
# --------------------------------------------------
print("=== Top 3 productos por cantidad vendida ===")
top_productos = (
    df.groupby("producto")["cantidad"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print(top_productos.to_string())
print()

# --------------------------------------------------
# 7. Ventas por vendedor y por mes (resumen cruzado)
# --------------------------------------------------
# En Excel: esto lo haría una tabla dinámica
# En Python: .groupby() con múltiples columnas

print("=== Ventas por vendedor y mes ===")
por_vendedor_mes = (
    df.groupby(["vendedor", "mes"])["total"]
    .sum()
    .reset_index()
    .sort_values(["vendedor", "mes"])
)
print(por_vendedor_mes.to_string(index=False))
