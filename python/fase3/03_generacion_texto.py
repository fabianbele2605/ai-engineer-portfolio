from transformers import pipeline

generador = pipeline("text-generation", model="distilgpt2")

prompt = "Artificial intelligence will change the world by"

resultado = generador(
    prompt,
    max_new_tokens=50,
    num_return_sequences=2,
    truncation=True
)

for i, r in enumerate(resultado):
    print(f"--- Opción {i+1} ---")
    print(r["generated_text"])
    print()