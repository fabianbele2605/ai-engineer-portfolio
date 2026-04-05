from transformers import AutoTokenizer

# Cargar tokenizador de un modelo real
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

texto = "Hello, I am learning about transformers and LLMs!"

# Tokenizar
tokens = tokenizer.tokenize(texto)
ids = tokenizer.encode(texto)

print(f"Texto original: {texto}")
print(f"\nTokens: {tokens}")
print(f"Total tokens: {len(tokens)}")
print(f"\nIDs numéricos: {ids}")
print(f"\nDecodificado: {tokenizer.decode(ids)}")