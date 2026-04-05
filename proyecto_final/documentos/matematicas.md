# 📐 Fase 1 - Matemáticas para ML

## Estadística Básica

```python
import numpy as np

datos = np.array([3, 5, 2, 8, 4, 7, 1, 9, 6, 5])

np.mean(datos)    # media → promedio
np.median(datos)  # mediana → valor del medio
np.std(datos)     # desviación estándar → qué tan dispersos están los datos
np.var(datos)     # varianza → desv. estándar al cuadrado
```

| Concepto | Descripción | En ML |
|---|---|---|
| Media | Promedio de todos los valores | Se afecta por valores extremos |
| Mediana | Valor del medio | Más robusta que la media |
| Desv. estándar | Dispersión respecto a la media | Indica si los datos están muy dispersos |
| Varianza | Desv. estándar al cuadrado | Misma idea que desv. estándar |

> 💡 Si Media ≈ Mediana, los datos están bien distribuidos. Si son muy diferentes, hay valores extremos.

---

## Probabilidad

```python
lanzamientos = np.random.randint(0, 2, 1000)  # 1000 valores de 0 o 1

prob = np.sum(lanzamientos == 1) / len(lanzamientos)
```

> 💡 Los modelos de clasificación no dicen "esto es un gato", dicen "hay 92% de probabilidad de que sea un gato".

**Ley de los grandes números** → con más datos, la probabilidad se acerca al valor real teórico.

---

## Álgebra Lineal

### Vectores

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b            # suma elemento a elemento
a * b            # multiplicación elemento a elemento
np.dot(a, b)     # producto punto → 1×4 + 2×5 + 3×6 = 32
```

> 💡 El **producto punto** es la operación más importante en redes neuronales. Cada neurona multiplica sus entradas por sus pesos y suma todo.

### Matrices

```python
M = np.array([[1, 2], [3, 4]])
N = np.array([[5, 6], [7, 8]])

np.dot(M, N)   # multiplicación de matrices
M.T            # transpuesta → voltear filas por columnas
```

> 💡 Una capa de neuronas procesa datos como una multiplicación de matrices. Por eso las GPUs son clave en ML, están optimizadas para esto.

---

## Normalización

Escalar datos antes de entrenar un modelo es obligatorio.

```python
precios = np.array([100, 200, 150, 300, 250])

# Min-Max → rango [0, 1]
normalizado = (precios - precios.min()) / (precios.max() - precios.min())

# Estandarización → media=0, desv=1
estandarizado = (precios - precios.mean()) / precios.std()
```

| Técnica | Resultado | Cuándo usar |
|---|---|---|
| Min-Max | Rango `[0, 1]` | Cuando conoces el rango de los datos |
| Estandarización | Media=0, Desv=1 | Cuando los datos siguen distribución normal |

> 💡 Sin normalizar, el modelo le da más importancia a variables con números grandes solo por su escala, no por su relevancia real.

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `matematicas/01_estadistica.py` | Media, mediana, moda, varianza, probabilidad |
| `matematicas/02_algebra_lineal.py` | Vectores, matrices, normalización |
