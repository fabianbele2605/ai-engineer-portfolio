from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Cargar datos
iris = load_iris()
X = iris.data  # características (tamaño pétalos/sépalos)
y = iris.target  # etiquetas (0=setosa, 1=versicolor, 2=virginica)

print(f"Total de muestras: {len(X)}")
print(f"Característica por muestra: {X.shape[1]}")
print(f"Clases: {iris.target_names}")

# 2. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nEntrenamiento: {len(X_train)} muestras")
print(f"Prueba:        {len(X_test)} muestras")

# 3. Crear y entrenar modelo
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

# 4. Evaluar
predicciones = modelo.predict(X_test)
accuracy = accuracy_score(y_test, predicciones)
print(f"\nAccuracy: {accuracy:.2%}")

from sklearn.metrics import classification_report, confusion_matrix

print("\n=== Reporte completo ===")
print(classification_report(y_test, predicciones, target_names=iris.target_names))

print("=== Matriz de confusión ===")
print(confusion_matrix(y_test, predicciones))
