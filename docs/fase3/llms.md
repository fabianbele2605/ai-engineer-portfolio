# 🧠 Fase 3 - LLMs y Transformers

## ¿Qué es un Transformer?

- **2017** → Google publica "Attention is All You Need"
- **2020** → GPT-3, los LLMs explotan
- **2022** → ChatGPT, el mundo cambia

En lugar de leer texto palabra por palabra, los Transformers leen **todo a la vez** y calculan qué palabras son más relevantes entre sí → **Attention**.

---

## Tokenización

Convierte texto en números porque los modelos solo entienden números.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

tokens = tokenizer.tokenize("Hello LLMs!")   # ['hello', 'll', '##ms', '!']
ids = tokenizer.encode("Hello LLMs!")        # [101, 7592, 2222, 5244, 999, 102]
texto = tokenizer.decode(ids)                # [CLS] hello llms! [SEP]
```

| Concepto | Descripción |
|---|---|
| `##ms` | Continuación de palabra, no estaba en vocabulario |
| `[CLS]` | Token especial de inicio |
| `[SEP]` | Token especial de fin |
| IDs | Cada token tiene un número único en el vocabulario |

> 💡 Diferentes modelos tienen diferentes tokenizadores. GPT usa BPE, BERT usa WordPiece.

---

## Pipelines de Hugging Face

```python
from transformers import pipeline

# Análisis de sentimiento
clasificador = pipeline("sentiment-analysis")
resultado = clasificador("I love AI!")[0]
# {'label': 'POSITIVE', 'score': 0.9999}

# Generación de texto
generador = pipeline("text-generation", model="distilgpt2")
resultado = generador("AI will change", max_new_tokens=50)

# Zero-shot classification
clasificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
resultado = clasificador(texto, candidate_labels=["programming", "cooking", "sports"])
```

| Pipeline | Tarea |
|---|---|
| `sentiment-analysis` | Positivo/Negativo |
| `text-generation` | Completar texto |
| `zero-shot-classification` | Clasificar sin entrenamiento previo |
| `question-answering` | Responder preguntas |
| `summarization` | Resumir texto |

---

## Zero-shot Classification

Clasificar en categorías **sin ejemplos de entrenamiento**.

```python
clasificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

resultado = clasificador(
    "I need to fix a bug in my Python code",
    candidate_labels=["programming", "cooking", "sports"]
)
# programming: 71.91%, technology: 26.23%, ...
```

> 💡 Con ML clásico necesitarías miles de ejemplos por categoría. Con zero-shot simplemente escribes las categorías en texto.

---

## Inferencia vs Entrenamiento

| | Inferencia | Entrenamiento |
|---|---|---|
| Qué hace | Usa el modelo para predecir | Ajusta los pesos del modelo |
| Recursos | Menos RAM/GPU | Mucha RAM/GPU |
| Tiempo | Segundos | Horas/días |
| Cuándo | Producción | Una vez |

---

## Archivos de práctica

| Archivo | Concepto |
|---|---|
| `python/fase3/01_tokenizacion.py` | Tokenización con BERT |
| `python/fase3/02_pipeline.py` | Sentiment analysis |
| `python/fase3/03_generacion_texto.py` | Generación de texto con GPT-2 |
| `python/fase3/04_zero_shot.py` | Zero-shot classification |
