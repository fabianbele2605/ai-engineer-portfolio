from transformers import pipeline

# Análisis de sentamiento
print("=== Análisis de Sentimiento ===")
clasificador = pipeline("sentiment-analysis")

textos = [
    "I love learning about AI, it's amazing!",
    "This is terrible, I hate it.",
    "The weather is okay today."
]

for texto in textos:
    resultado = clasificador(texto)[0]
    print(f"{texto}")
    print(f" -> {resultado['label']} ({resultado['score']:.2%})\n")
    