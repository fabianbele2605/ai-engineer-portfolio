import numpy as np
import pandas as pd

# --- NUMPY: operaciones matematicas rapidas ---
horas = np.array([3, 5, 8, 4])

print("=== Numpy ===")
print(f"Promedio: {np.mean(horas):.1f}")
print(f"Maximo: {np.max(horas)}")
print(f"Mínimo: {np.min(horas)}")
print(f"Desviación estándar: {np.std(horas):.2f}")

# --- PANDAS: análisis de datos con tablas ---
print("\n=== Pandas ===")
df = pd.read_csv("matematicas/datos.csv")

print(df)
print(f"\nPromedio horas: {df['horas_estudio'].mean():.1f}")
print(f"\nEstudiantes por fase:")
print(df.groupby("fase_actual")["nombre"].count())