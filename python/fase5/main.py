import faiss
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI(title="AI Engineer API")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

conocimiento = [
    "Python is a high-level programming language great for AI and ML",
    "FastAPI is a modern web framework for building APIs with Python",
    "Docker containers allow you to package applications consistently",
    "Machine learning models learn patterns from training data",
    "RAG combines retrieval systems with language model generation",
    "AWS provides cloud computing services for deploying applications",
    "Rust is a systems programming language focused on performance and safety",
    "Git is a version control system for tracking code changes",
]

# Indexar documentos al iniciar
embeddings = embedder.encode(conocimiento).astype("float32")
indice = faiss.IndexFlatL2(embeddings.shape[1])
indice.add(embeddings)

class Pregunta(BaseModel):
    texto: str
    k: int = 2

@app.get("/health")
def health():
    return {"status": "ok", "documentos": len(conocimiento)}

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando!", "documentos_indexados": len(conocimiento)}

@app.get("/documentos")
def listar_documentos():
    return {"total": len(conocimiento), "documentos": conocimiento}

@app.post("/buscar")
def buscar(pregunta: Pregunta):
    if not pregunta.texto.strip():
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía")
    if pregunta.k < 1 or pregunta.k > len(conocimiento):
        raise HTTPException(status_code=400, detail=f"k debe estar entre 1 y {len(conocimiento)}")
    vector = embedder.encode([pregunta.texto]).astype("float32")
    distancias, indices = indice.search(vector, pregunta.k)
    resultados = [
        {"documento": conocimiento[i], "distancia": float(d)}
        for i, d in zip(indices[0], distancias[0])
    ]
    return {"pregunta": pregunta.texto, "resultados": resultados}
