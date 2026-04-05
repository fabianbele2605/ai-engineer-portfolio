# 🧪 Fase 4 - AI Aplicada (RAG + Embeddings)

## ¿Qué es RAG?

RAG (Retrieval Augmented Generation) es cómo funcionan los chatbots que responden preguntas sobre documentos.

```
1. Tienes documentos (PDFs, TXTs, etc.)
2. Los conviertes en embeddings (vectores numéricos)
3. Los guardas en una base vectorial (FAISS)
4. El usuario hace una pregunta
5. Buscas los fragmentos más similares
6. Se los das al LLM como contexto
7. El LLM responde basándose en esos fragmentos
```

---

## Embeddings

Convierte texto en vectores numéricos que capturan el **significado semántico**.

```python
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = modelo.encode(["Hello world", "Hi there"])
# shape: (2, 384) → 2 frases, 384 dimensiones cada una
```

### Similitud coseno

```python
import numpy as np

def similitud(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

> 💡 Frases con significado similar tendrán vectores similares aunque usen palabras diferentes. Esto es búsqueda semántica.

---

## FAISS - Base vectorial

Indexa y busca embeddings eficientemente.

```python
import faiss

# Crear índice
indice = faiss.IndexFlatL2(dimension)  # L2 = distancia euclidiana
indice.add(embeddings)                 # agregar vectores

# Buscar los k más cercanos
vector = modelo.encode(["mi pregunta"]).astype("float32")
distancias, indices = indice.search(vector, k=3)
```

| Método | Descripción |
|---|---|
| `IndexFlatL2` | Búsqueda exacta por distancia euclidiana |
| `IndexFlatIP` | Búsqueda por producto interno (similitud coseno) |
| `IndexIVFFlat` | Búsqueda aproximada, más rápida para millones de vectores |

---

## RAG completo

```python
def rag(pregunta, k=2):
    # 1. Recuperar documentos relevantes
    vector = embedder.encode([pregunta]).astype("float32")
    _, indices = indice.search(vector, k)
    contexto = " ".join([documentos[i] for i in indices[0]])

    # 2. Generar respuesta con contexto
    prompt = f"Context: {contexto}\nQuestion: {pregunta}\nAnswer:"
    respuesta = generador(prompt, max_new_tokens=80)[0]["generated_text"]
    return respuesta
```

> 💡 La calidad de la respuesta depende del LLM. Con modelos pequeños (distilgpt2) las respuestas son limitadas. Con GPT-4 o Claude son precisas y coherentes.

---

## Limitaciones y soluciones

| Problema | Solución |
|---|---|
| Modelo pequeño → respuestas pobres | Usar API de OpenAI/Anthropic/AWS Bedrock |
| Documentos largos | Dividir en chunks de ~500 tokens |
| Muchos documentos | Usar `IndexIVFFlat` en lugar de `IndexFlatL2` |

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `python/fase4/01_embeddings.py` | Embeddings + similitud semántica |
| `python/fase4/02_faiss.py` | Búsqueda vectorial con FAISS |
| `python/fase4/03_rag.py` | Pipeline RAG completo |
