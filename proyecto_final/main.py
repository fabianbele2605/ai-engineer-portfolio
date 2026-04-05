import os
import json
import faiss
import boto3
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI(title="Chat con Documentos - RAG + Claude", version="2.0")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

def cargar_documentos(carpeta="documentos"):
    chunks, fuentes = [], []
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
print(f"✅ {len(chunks)} fragmentos indexados")

def llamar_claude(pregunta: str, contexto: str) -> str:
    prompt = f"""You are a helpful AI assistant. Answer the question based only on the provided context.
If the answer is not in the context, say "I don't have enough information to answer that."

Context:
{contexto}

Question: {pregunta}

Answer:"""

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    })

    response = bedrock.invoke_model(modelId=MODEL_ID, body=body)
    result = json.loads(response["body"].read())
    return result["content"][0]["text"]

class Pregunta(BaseModel):
    texto: str
    k: int = 3

@app.get("/")
def inicio():
    return {"app": "Chat con Documentos RAG + Claude", "fragmentos": len(chunks)}

@app.get("/health")
def health():
    return {"status": "ok", "fragmentos": len(chunks)}

@app.get("/documentos")
def listar_documentos():
    resumen = {}
    for fuente in fuentes:
        resumen[fuente] = resumen.get(fuente, 0) + 1
    return {"documentos": resumen}

@app.post("/chat")
def chat(pregunta: Pregunta):
    if not pregunta.texto.strip():
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía")

    vector = embedder.encode([pregunta.texto]).astype("float32")
    distancias, indices = indice.search(vector, pregunta.k)

    contexto_chunks = [chunks[i] for i in indices[0]]
    fuentes_resultado = [fuentes[i] for i in indices[0]]
    contexto = "\n".join(contexto_chunks)

    respuesta = llamar_claude(pregunta.texto, contexto)

    return {
        "pregunta": pregunta.texto,
        "respuesta": respuesta,
        "contexto": contexto_chunks,
        "fuentes": fuentes_resultado
    }
