import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Datos: horas de estudio -> puntaje examen
np.random.seed(42)
horas = np.random.uniform(1, 10, 100).reshape(-1, 1)
puntaje = 10 * horas + np.random.normal(0, 5, (100, 1))

# Dividir, entrenar, evaluar
X_train, X_test, y_train, y_test = train_test_split(horas, puntaje, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)

print(f"R² Score: {r2_score(y_test, predicciones):.4f}")
print(f"Error cuadrático medio: {mean_squared_error(y_test, predicciones):.2f}")
print(f"\nSi estudias 8 horas, tu puntaje será: {modelo.predict([[8]])[0][0]:.1f}")

# Gráfica
plt.scatter(X_test, y_test, color="blue", label="Real")
plt.plot(X_test, predicciones, color="red", label="Predicción")
plt.xlabel("Horas de estidio")
plt.ylabel("Puntaje")
plt.legend()
plt.savefig("fase2/regresion.png")
print("\nGrafica guardada en fase2/regresion.png")
