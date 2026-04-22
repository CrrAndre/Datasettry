# Datasettry 📊

Repositorio de aprendizaje para **data entry y análisis de datos** con Python, pensado para personas que ya tienen bases en Excel y tablas dinámicas.

---

## 🎯 ¿Para quién es este repositorio?

- Personas que están empezando con Python
- Quienes ya saben usar Excel y tablas dinámicas
- Estudiantes de data entry y análisis de datos

---

## 📁 Estructura del proyecto

```
Datasettry/
│
├── datasets/               # Archivos CSV de práctica
│   └── ventas.csv          # Dataset de ventas de ejemplo
│
├── scripts/                # Scripts de Python para aprender paso a paso
│   ├── 01_leer_datos.py         # Cómo leer y explorar un CSV
│   ├── 02_limpieza_datos.py     # Limpiar y preparar datos
│   ├── 03_analisis_basico.py    # Estadísticas y resúmenes
│   └── 04_tablas_dinamicas.py   # Tablas dinámicas con pandas (pivot tables)
│
└── README.md
```

---

## 🚀 Primeros pasos

### 1. Instalar Python y las librerías necesarias

Asegúrate de tener Python 3 instalado. Luego instala las dependencias:

```bash
pip install pandas openpyxl
```

### 2. Ejecutar los scripts en orden

```bash
python scripts/01_leer_datos.py
python scripts/02_limpieza_datos.py
python scripts/03_analisis_basico.py
python scripts/04_tablas_dinamicas.py
```

---

## 📚 Conexión entre Excel y Python

| Excel                        | Python (pandas)                          |
|------------------------------|------------------------------------------|
| Abrir un archivo `.csv`      | `pd.read_csv("archivo.csv")`             |
| Ver las primeras filas       | `df.head()`                              |
| Filtrar filas                | `df[df["columna"] == "valor"]`           |
| Suma de una columna          | `df["columna"].sum()`                    |
| Tabla dinámica               | `df.pivot_table(...)`                    |
| Agrupar y calcular           | `df.groupby("columna").sum()`            |
| Ordenar datos                | `df.sort_values("columna")`              |
| Eliminar duplicados          | `df.drop_duplicates()`                   |
| Rellenar celdas vacías       | `df.fillna(0)` o `df.dropna()`           |

---

## 💡 Recursos para seguir aprendiendo

- [Documentación oficial de pandas (en inglés)](https://pandas.pydata.org/docs/)
- [Tutorial de pandas en español](https://aprendeconalf.es/docencia/python/manual/pandas/)
- [Python para análisis de datos – libro gratuito](https://wesmckinney.com/book/)
