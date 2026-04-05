import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

np.random.seed(42)
X = np.sort(np.random.uniform(0, 10, 30))
y = np.sin(X) + np.random.normal(0, 0.3, 30)

X = X.reshape(-1, 1)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
grados = [1, 4, 15]
nombres = ["Underfitting (grado 1)", "Correcto (grado 4)", "Overfitting (grado 15)"]

for ax, grado, nombre in zip(axes, grados, nombres):
    modelo = Pipeline([
        ("poly", PolynomialFeatures(degree=grado)),
        ("linear", LinearRegression())
    ])
    modelo.fit(X, y)
    X_plot = np.linspace(0, 10, 300).reshape(-1, 1)
    y_plot = modelo.predict(X_plot)
    r2 = r2_score(y, modelo.predict(X))

    ax.scatter(X, y, color="blue", s=20)
    ax.plot(X_plot, y_plot, color="red")
    ax.set_title(f"{nombre}\nR²={r2:.3f}")
    ax.set_ylim(-3, 3)

plt.tight_layout()
plt.savefig("fase2/overfitting.png")
print("Gráfica guardada en fase2/overfitting.png")
print("\nUnderfitting -> modelo muy simple, no aprende")
print("Correcto      -> modelo equilibrado")
print("Overfitting   -> modelo memoriza, falta con datos nuevos")