import os
import faiss
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI(title="Chat con Documentos - RAG", version="1.0")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# --- Cargar y chunking de documentos ---
def cargar_documentos(carpeta="documentos"):
    chunks = []
    fuentes = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            with open(f"{carpeta}/{archivo}", "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        chunks.append(linea)
                        fuentes.append(archivo.replace(".txt", ""))
    return chunks, fuentes

chunks, fuentes = cargar_documentos()
embeddings = embedder.encode(chunks).astype("float32")
indice = faiss.IndexFlatL2(embeddings.shape[1])
indice.add(embeddings)

print(f"✅ {len(chunks)} fragmentos indexados de {len(set(fuentes))} documentos")

# --- Modelos ---
class Pregunta(BaseModel):
    texto: str
    k: int = 3

class Respuesta(BaseModel):
    pregunta: str
    contexto: list[str]
    fuentes: list[str]

# --- Endpoints ---
@app.get("/")
def inicio():
    return {
        "app": "Chat con Documentos RAG",
        "fragmentos_indexados": len(chunks),
        "documentos": list(set(fuentes))
    }

@app.get("/health")
def health():
    return {"status": "ok", "fragmentos": len(chunks)}

@app.get("/documentos")
def listar_documentos():
    resumen = {}
    for chunk, fuente in zip(chunks, fuentes):
        resumen.setdefault(fuente, 0)
        resumen[fuente] += 1
    return {"documentos": resumen}

@app.post("/chat", response_model=Respuesta)
def chat(pregunta: Pregunta):
    if not pregunta.texto.strip():
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía")

    vector = embedder.encode([pregunta.texto]).astype("float32")
    distancias, indices = indice.search(vector, pregunta.k)

    contexto = [chunks[i] for i in indices[0]]
    fuentes_resultado = [fuentes[i] for i in indices[0]]

    return Respuesta(
        pregunta=pregunta.texto,
        contexto=contexto,
        fuentes=fuentes_resultado
    )
