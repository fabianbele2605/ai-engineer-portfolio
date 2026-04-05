# 🤖 Fase 2 - Machine Learning

## Flujo base de todo ML

```
1. Cargar datos
2. Dividir en entrenamiento y prueba
3. Normalizar
4. Entrenar modelo
5. Evaluar métricas
```

> 💡 Siempre estos 5 pasos en ese orden.

---

## Tipos de aprendizaje

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Supervisado | Datos con etiquetas correctas | Clasificar fotos de gatos/perros |
| No supervisado | El modelo encuentra patrones solo | Agrupar clientes por comportamiento |

---

## Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

- `test_size=0.2` → 80% entrenamiento, 20% prueba
- Nunca evalúes con los mismos datos que entrenaste

---

## Normalización antes de entrenar

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # aprende la escala y transforma
X_test = scaler.transform(X_test)        # solo transforma, no aprende
```

> 💡 `fit_transform` solo en train, `transform` en test. Si haces fit en test estás haciendo trampa.

---

## Modelos de Clasificación

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
```

| Modelo | Ventaja | Cuándo usar |
|---|---|---|
| Regresión Logística | Simple y rápido | Datos linealmente separables |
| Árbol de Decisión | Interpretable | Cuando necesitas explicar decisiones |
| Random Forest | Robusto y preciso | Mayoría de casos ✅ |

---

## Regresión Lineal

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)

r2_score(y_test, predicciones)           # 0 a 1, más alto mejor
mean_squared_error(y_test, predicciones) # error promedio al cuadrado
```

---

## Métricas

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

accuracy_score(y_test, predicciones)                    # % de aciertos
classification_report(y_test, predicciones)             # precision, recall, f1
confusion_matrix(y_test, predicciones)                  # matriz de errores
```

| Métrica | Descripción |
|---|---|
| Accuracy | % total de aciertos |
| Precision | De lo que predijo como X, ¿cuántos eran X? |
| Recall | De todos los X reales, ¿cuántos encontró? |
| F1-score | Balance entre precision y recall |

---

## Cross-Validation

```python
from sklearn.model_selection import cross_val_score

score = cross_val_score(modelo, X_train, y_train, cv=5).mean()
```

> 💡 Divide los datos en 5 partes y entrena/evalúa 5 veces. Más confiable que un solo split.

---

## Overfitting vs Underfitting

| Problema | Síntoma | Solución |
|---|---|---|
| Underfitting | CV Score bajo | Modelo más complejo |
| Overfitting | CV Score alto, Test Score bajo | Más datos, regularización |
| Correcto | CV Score ≈ Test Score | ✅ |

---

## Guardar y cargar modelos

```python
import joblib

# Guardar
joblib.dump(modelo, "modelo.pkl")
joblib.dump(scaler, "scaler.pkl")

# Cargar
modelo = joblib.load("modelo.pkl")
scaler = joblib.load("scaler.pkl")
```

> 💡 En producción cargas el modelo una vez al iniciar la API y lo usas para miles de predicciones.

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `fase2/01_primer_modelo.py` | Clasificación KNN + métricas |
| `fase2/02_regresion.py` | Regresión lineal + R² |
| `fase2/03_overfitting.py` | Overfitting vs Underfitting |
| `fase2/04_clasificador.py` | Comparar modelos + guardar/cargar |
