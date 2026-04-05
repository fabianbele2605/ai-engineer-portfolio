import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# 1. Base de conocimiento
documentos = [
    "Python is a high-level programming language great for AI and ML",
    "FastAPI is a modern web framework for building APIs with Python",
    "Docker containers allow you to package applications consistently",
    "Machine learning models learn patterns from training data",
    "RAG combines retrieval systems with language model generation",
    "Neural networks are inspired by the human brain structure",
    "AWS provides cloud computing services for deploying applications"
]

# 2. Indexar con FAISS
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(documentos).astype("float32")
indice = faiss.IndexFlatL2(embeddings.shape[1])
indice.add(embeddings)

# 3. LLM para generar respuesta
generador = pipeline("text-generation", model="distilgpt2")

def rag(pregunta, k=2):
    # Recuperar documentos relevantes
    vector = embedder.encode([pregunta]).astype("float32")
    _, indices = indice.search(vector, k)
    contexto = " ".join([documentos[i] for i in indices[0]])

    # Generar respuesta con contexto
    prompt = f"Context: {contexto}\nQuestion: {pregunta}\nAnswer:"
    respuesta = generador(prompt, max_new_tokens=80, truncation=True)[0]['generated_text']

    print(f"\nPregunta: {pregunta}")
    print(f"Contexto usado: {contexto[:100]}...")
    print(f"Respuesta: {respuesta}")

rag("What is RAG in AI")
rag("How can I build an API with Python?")