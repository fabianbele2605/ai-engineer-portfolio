from sentence_transformers import SentenceTransformer
import numpy as np

modelo = SentenceTransformer("all-MiniLM-L6-v2")

frases = [
    "I love programming in Python",
    "Python is my favorite language",
    "I enjoy playing football",
    "Soccer is a great sport",
    "Machine learning is fascinating"
]

embedding = modelo.encode(frases)

print(f"Dimesión de cada embedding: {embedding.shape[1]}")
print(f"Total de frases: {embedding.shape[0]}\n")

# Similitud entre frases
def similitud(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

base = embedding[0]     # "I love programming is Python"
print(f"Frase base: '{frases[0]}\n'")

for i, (frases, emb) in enumerate(zip(frases[1:], embedding[1:]), 1):
    sim = similitud(base, emb)
    barra = "█" * int(sim * 30)
    print(f"{frases}")
    print(f" Similitud: {sim:.4f} {barra}\n")