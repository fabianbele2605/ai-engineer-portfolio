from transformers import pipeline

clasificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

texto = "I need fix a bug in my Python code that crashes the server"

categorias = ["programming", "cooking", "sports", "technology", "medicine"]

resultado = clasificador(texto, candidate_labels=categorias)

print(f"Texto: {texto}\n")
for label, score in zip(resultado["labels"], resultado["scores"]):
    barra = "█" * int(score * 30)
    print(f"{label:<15} {score:.2%} {barra}")
