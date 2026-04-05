# 🤖 AI Engineer Portfolio

> RAG-based document chat system built with FastAPI, FAISS, and Sentence Transformers.

## 🚀 Demo

```bash
# Run with Docker
docker build -t chat-documentos ./proyecto_final
docker run -p 8000:8000 chat-documentos

# Open API docs
http://localhost:8000/docs
```

---

## 🏗️ Architecture

```
User Question
     │
     ▼
[FastAPI API]
     │
     ▼
[Sentence Transformers]  ← converts question to embedding
     │
     ▼
[FAISS Vector Search]    ← finds most similar document chunks
     │
     ▼
[Relevant Context]       ← returns top-k fragments + sources
```

---

## 📁 Project Structure

```
ai-engineer-portfolio/
├── proyecto_final/          ← 🏁 Final project (RAG Chat)
│   ├── main.py              ← FastAPI + FAISS + RAG
│   ├── Dockerfile
│   ├── requirements.txt
│   └── documentos/          ← knowledge base
│       ├── python.txt
│       ├── ml.txt
│       ├── aws.txt
│       └── azure.txt
├── python/                  ← Practice scripts by phase
│   ├── fase1/               ← Python fundamentals
│   ├── fase2/               ← Machine Learning
│   ├── fase3/               ← LLMs & Transformers
│   ├── fase4/               ← RAG & Embeddings
│   └── fase5/               ← FastAPI Backend
├── matematicas/             ← Math for ML
├── docs/                    ← Documentation per phase
└── Dockerfile               ← Global Docker config
```

---

## 🧠 What I Built

### Phase 1 - Python & Math
- Data structures, OOP, file handling
- Statistics, linear algebra, normalization with NumPy/Pandas

### Phase 2 - Machine Learning
- Classification and regression models with Scikit-learn
- Cross-validation, metrics (accuracy, F1, confusion matrix)
- Overfitting vs underfitting

### Phase 3 - LLMs & Transformers
- Tokenization with BERT
- Sentiment analysis, text generation, zero-shot classification
- Hugging Face pipelines

### Phase 4 - Applied AI (RAG)
- Semantic embeddings with Sentence Transformers
- Vector search with FAISS
- Full RAG pipeline

### Phase 5 - Backend
- REST API with FastAPI
- Data validation with Pydantic
- Error handling and `/health` endpoint

### Phase 6 - Deployment
- Dockerized application
- Ready for AWS App Runner / ECS deployment

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.12 |
| ML/AI | PyTorch, Scikit-learn, Transformers |
| Embeddings | Sentence Transformers, FAISS |
| Backend | FastAPI, Uvicorn, Pydantic |
| DevOps | Docker |
| Cloud | AWS (ECR, App Runner) |

---

## ⚡ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | App info + indexed fragments |
| GET | `/health` | Health check |
| GET | `/documentos` | List documents and chunk count |
| POST | `/chat` | Semantic search over documents |

### Example Request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"texto": "What is AWS Lambda?", "k": 3}'
```

### Example Response

```json
{
  "pregunta": "What is AWS Lambda?",
  "contexto": [
    "AWS Lambda allows running code without managing servers, paying only for execution time.",
    "AWS is Amazon Web Services, the world's most comprehensive cloud computing platform.",
    "Azure Functions is a serverless compute service similar to AWS Lambda."
  ],
  "fuentes": ["aws", "aws", "azure"]
}
```

---

## 📚 Learning Path

This portfolio was built following an intensive 4-6 month AI Engineer roadmap:

| Phase | Topic | Status |
|---|---|---|
| 1 | Python + Math Fundamentals | ✅ |
| 2 | Machine Learning | ✅ |
| 3 | LLMs & Transformers | ✅ |
| 4 | Applied AI (RAG, Embeddings) | ✅ |
| 5 | Backend + Integration | ✅ |
| 6 | Deployment & Production | ✅ |

---

## 👤 Author

**Fabian Beleño**
- GitHub: [@fabianbele2605](https://github.com/fabianbele2605)
