import numpy as np

# Vectores -> listas de números
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("=== Vectores ===")
print(f"Suma:            {a + b}")
print(f"Resta:           {a - b}")
print(f"Multiplicar:     {a * b}")
print(f"Producto punto: {np.dot(a, b)}")   # muy usado en redes neuronales

# Matrices -> tablas de números
print("\n=== Matrices ===")
M = np.array([[1, 2], [3, 4]])
N = np.array([[5, 6], [7, 8]])

print(f"Matriz M:\n{M}")
print(f"Multiplicación de matrices: \n{np.dot(M, N)}")
print(f"Transpuesta de M:\n{M.T}")


# Normalización -> escalar datos al rango [0, 1]
print("\n=== Normalizacion ===")
precios = np.array([100, 200, 150, 300, 250])

# Min-Max normalization
normalizado = (precios - precios.min()) / (precios.max() - precios.min())
print(f"Original:    {precios}")
print(f"Normalizado: {normalizado}")

# Estandarización -> media=0, desv=1
estandarizado = (precios -precios.mean()) / precios.std()
print(f"Estandarizado: {estandarizado.round(2)}")