import numpy as np
import joblib
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Crear dataset más complejo
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    random_state=42
)

# 2. Dividir y normalizar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Comparar 3 modelos
modelos = {
    "Regresión Logística": LogisticRegression(),
    "Arbol de Decisión": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    score = cross_val_score(modelo, X_train, y_train, cv=5).mean()
    test_score = modelo.score(X_test, y_test)
    print(f"{nombre}")
    print(f" CV Score:   {score:.2%}")
    print(f" Test Score: {test_score:.2%}\n")


# Guardar el mejor modelo
mejor_modelo = modelos["Random Forest"]
joblib.dump(mejor_modelo, "fase2/modelo_rf.pkl")
joblib.dump(scaler, "fase2/scaler.pkl")
print("Modelo guardado!")

# Cargar y usar 
modelo_cargado = joblib.load("fase2/modelo_rf.pkl")
scaler_cargado = joblib.load("fase2/scaler.pkl")

muestra = X_test[0].reshape(1, -1)
prediccion = modelo_cargado.predict(muestra)
print(f"Predicción con modelo cargado: clase {prediccion[0]}")