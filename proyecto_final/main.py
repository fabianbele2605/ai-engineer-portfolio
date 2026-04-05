import os
import json
import faiss
import boto3
import numpy as np
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Session

app = FastAPI(title="Chat con Documentos - RAG + Claude", version="3.0")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

# --- Base de datos ---
engine = create_engine("sqlite:///historial.db")

class Base(DeclarativeBase):
    pass

class Conversacion(Base):
    __tablename__ = "conversaciones"
    id = Column(Integer, primary_key=True)
    pregunta = Column(Text)
    respuesta = Column(Text)
    fuentes = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

# --- Documentos ---
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

# --- Modelos ---
class Pregunta(BaseModel):
    texto: str
    k: int = 3

# --- Endpoints ---
@app.get("/")
def inicio():
    return {"app": "Chat con Documentos RAG + Claude", "version": "3.0", "fragmentos": len(chunks)}

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

    try:
        respuesta = llamar_claude(pregunta.texto, contexto)
    except Exception:
        respuesta = f"Contexto encontrado: {contexto_chunks[0]}"

    with Session(engine) as session:
        session.add(Conversacion(
            pregunta=pregunta.texto,
            respuesta=respuesta,
            fuentes=",".join(fuentes_resultado)
        ))
        session.commit()

    return {
        "pregunta": pregunta.texto,
        "respuesta": respuesta,
        "contexto": contexto_chunks,
        "fuentes": fuentes_resultado
    }

@app.get("/historial")
def historial():
    with Session(engine) as session:
        conversaciones = session.query(Conversacion).order_by(Conversacion.fecha.desc()).limit(10).all()
        return {"historial": [
            {
                "id": c.id,
                "pregunta": c.pregunta,
                "respuesta": c.respuesta,
                "fuentes": c.fuentes,
                "fecha": c.fecha
            }
            for c in conversaciones
        ]}
