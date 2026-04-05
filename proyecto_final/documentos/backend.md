# ⚙️ Fase 5 - Backend con FastAPI

## ¿Qué es FastAPI?

Framework moderno para construir APIs con Python. Genera documentación automática y es el más usado en proyectos de IA.

---

## Estructura básica

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mi API")

# Modelo de datos con Pydantic
class Pregunta(BaseModel):
    texto: str
    k: int = 2  # valor por defecto

# Endpoints
@app.get("/")           # GET
@app.post("/buscar")    # POST
@app.get("/health")     # monitoreo
```

---

## Endpoints

```python
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/buscar")
def buscar(pregunta: Pregunta):
    if not pregunta.texto.strip():
        raise HTTPException(status_code=400, detail="Pregunta vacía")
    # lógica...
    return {"resultado": "..."}
```

| Método | Uso |
|---|---|
| `GET` | Obtener datos |
| `POST` | Enviar datos / procesar |
| `PUT` | Actualizar |
| `DELETE` | Eliminar |

---

## Pydantic - Validación de datos

```python
from pydantic import BaseModel

class Pregunta(BaseModel):
    texto: str        # obligatorio
    k: int = 2        # opcional con default
```

> 💡 Pydantic valida automáticamente los tipos. Si envías un número donde se espera texto, devuelve error 422 automáticamente.

---

## Integración con FAISS

```python
# Al iniciar la app, indexar documentos
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(documentos).astype("float32")
indice = faiss.IndexFlatL2(embeddings.shape[1])
indice.add(embeddings)

# En el endpoint, buscar
@app.post("/buscar")
def buscar(pregunta: Pregunta):
    vector = embedder.encode([pregunta.texto]).astype("float32")
    distancias, indices = indice.search(vector, pregunta.k)
    return {"resultados": [...]}
```

---

## Correr el servidor

```bash
# Desarrollo con auto-reload
uvicorn python.fase5.main:app --reload

# Producción
uvicorn python.fase5.main:app --host 0.0.0.0 --port 8000
```

| URL | Descripción |
|---|---|
| `http://localhost:8000` | API |
| `http://localhost:8000/docs` | Documentación interactiva (Swagger) |
| `http://localhost:8000/health` | Estado del servidor |

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `python/fase5/main.py` | API completa con FAISS + validación |
