# 🐍 Fase 1 - Python Fundamentos

## Variables y Tipos de datos

```python
nombre = "AI Engineer"   # str   → texto
version = 3.12           # float → número decimal
activo = True            # bool  → True o False
entero = 42              # int   → número entero
```

> Python detecta el tipo automáticamente, no necesitas declararlo.

---

## Listas y Diccionarios

```python
# Lista → colección ordenada
habilidades = ["Python", "ML", "LLMs"]
habilidades.append("Rust")       # agregar
habilidades[0]                   # acceder por índice

# Diccionario → clave:valor (equivalente a JSON)
perfil = {"nombre": "Fabian", "nivel": 1}
perfil["nivel"] += 1             # modificar
perfil["nuevo"] = "valor"        # agregar clave
```

---

## f-strings

```python
nombre = "Fabian"
print(f"Hola {nombre}!")         # forma moderna de insertar variables
print(f"Progreso: {16.7:.1f}%")  # :.1f → 1 decimal
```

---

## Funciones

```python
def saludar(nombre, rol="AI Engineer"):   # parámetro con valor por defecto
    return f"Hola {nombre}, eres un {rol}"

saludar("Fabian")                # usa el default
saludar("Fabian", "ML Engineer") # sobreescribe el default
```

---

## Clases

```python
class Estudiante:
    def __init__(self, nombre):  # constructor, se ejecuta al crear el objeto
        self.nombre = nombre     # self → referencia a la instancia
        self.temas = []

    def aprender(self, tema):
        self.temas.append(tema)

fabian = Estudiante("Fabian")    # crear instancia
fabian.aprender("Python")        # llamar método
```

---

## Manejo de Archivos JSON

```python
import json

# Escribir
with open("archivo.json", "w") as f:
    json.dump(datos, f, indent=2)

# Leer
with open("archivo.json", "r") as f:
    datos = json.load(f)
```

> `with open(...)` cierra el archivo automáticamente aunque haya un error.

---

## Manejo de Errores

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

| Error común | Cuándo ocurre |
|---|---|
| `FileNotFoundError` | Archivo no existe |
| `JSONDecodeError` | JSON mal formado |
| `ZeroDivisionError` | División entre cero |
| `KeyError` | Clave no existe en diccionario |
| `TypeError` | Tipo de dato incorrecto |

---

## NumPy

```python
import numpy as np

horas = np.array([3, 5, 2, 8, 4])

np.mean(horas)   # promedio
np.max(horas)    # máximo
np.min(horas)    # mínimo
np.std(horas)    # desviación estándar
```

> `np.array` es como una lista pero optimizada para matemáticas. Base de todo ML.

---

## Pandas

```python
import pandas as pd

df = pd.read_csv("datos.csv")         # cargar CSV como tabla
df["columna"].mean()                  # promedio de una columna
df.groupby("col")["otro"].count()     # agrupar datos
```

> `DataFrame` es como una hoja de Excel en Python.

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `python/01_fundamentos.py` | Variables, tipos, listas, diccionarios |
| `python/02_funciones.py` | Funciones y parámetros |
| `python/03_archivos.py` | Leer/escribir JSON |
| `python/04_clases.py` | Clases y objetos |
| `python/05_errores.py` | Try/Except |
| `python/06_csv.py` | CSV manual |
| `python/07_numpy_pandas.py` | NumPy + Pandas |
| `python/proyecto_fase1.py` | 🚧 Mini proyecto: tracker de progreso |
