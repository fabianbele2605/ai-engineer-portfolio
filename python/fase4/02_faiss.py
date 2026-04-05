import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Base de conocimiento
documentos = [
    "Python is a high-level programming language great for AI and ML",
    "FastAPI is a modern web framework for building APIs with Python",
    "Docker containers allow you to package applications consistently",
    "Machine learning models learn patterns from training data",
    "RAG combines retrieval systems with language model generation",
    "Neural networks are inspired by the human brain structure",
    "Git is a version control system for tracking code changes",
    "AWS provides cloud computing services for deploying applications",
]

# Crear embeddings e índices FAISS
embeddings = modelo.encode(documentos).astype("float32")
dimension = embeddings.shape[1]

indice = faiss.IndexFlatIP(dimension)
indice.add(embeddings)
print(f"Documentos indexados: {indice.ntotal}")

# Buscar 
def buscar(pregunta, k=3):
    vector = modelo.encode([pregunta]).astype("float32")
    distancias, indices = indice.search(vector, k)
    print(f"\nPregunta: {pregunta}")
    print("Resultados más revelantes:")
    for i, (idx, dist) in enumerate(zip(indices[0], distancias[0])):
        print(f"  {i+1}. {documentos[idx]}")

buscar("How do I deploy a Python application?")
buscar("What is machine learning?")