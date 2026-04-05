import numpy as np

datos = np.array([3, 5, 2, 8, 4, 7, 1, 9, 6, 5])

# Medidas de tendencia central
print(f"Media:    {np.mean(datos):.2f}")           # promedio
print(f"Mediana:  {np.median(datos):.2f}")         # valor del medio
print(f"Moda:     {np.bincount(datos).argmax()}")  # valor mas repetido

# Medidas de dispersión
print(f"\nDesv. estandar: {np.std(datos):.2f}")    #qué tan dispersos están
print(f"Varianza:       {np.var(datos):.2f}")      # desv. estándar al cuadrado
print(f"Rango:           {np.max(datos) - np.min(datos)}")  # máx - mín


# Probabilidad básica
print("\n=== Probabilidad ===")
lanzamientos = np.random.randint(0, 2, 1000)  # 1000 lanzamiento de moneda (0 o 1)

prob_cara = np.sum(lanzamientos == 1) / len(lanzamientos)
prob_sello = np.sum(lanzamientos == 0) / len(lanzamientos)

print(f"Probabilidad cara:  {prob_cara:.2f}")
print(f"Probabilidad sello: {prob_sello:.2f}")
print(f"Suma total:         {prob_cara + prob_sello:.2f}")

