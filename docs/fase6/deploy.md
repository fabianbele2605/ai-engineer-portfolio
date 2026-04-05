# 🚀 Fase 6 - Despliegue y Producción

## Docker

Empaqueta tu app con todas sus dependencias en un contenedor que corre igual en cualquier máquina.

### Dockerfile

```dockerfile
FROM python:3.12-slim          # imagen base

WORKDIR /app                   # directorio de trabajo

COPY requirements.txt .
RUN pip install --no-cache-dir fastapi uvicorn sentence-transformers faiss-cpu pydantic

COPY python/fase5/main.py .

EXPOSE 8000                    # puerto expuesto

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### .dockerignore

```
.venv
__pycache__
*.pyc
*.pkl
.git
```

> 💡 `.dockerignore` evita copiar archivos innecesarios a la imagen, haciéndola más pequeña y rápida de construir.

### Comandos esenciales

```bash
docker build -t mi-api .          # construir imagen
docker run -p 8000:8000 mi-api    # correr contenedor
docker ps                         # ver contenedores activos
docker stop <id>                  # detener contenedor
docker images                     # ver imágenes disponibles
docker logs <id>                  # ver logs del contenedor
```

---

## Deploy en AWS

### Opción 1: AWS App Runner (más simple)
```
1. Subir imagen a ECR (Elastic Container Registry)
2. Crear servicio en App Runner apuntando a la imagen
3. App Runner maneja el escalado automáticamente
```

### Opción 2: AWS ECS + Fargate (más control)
```
1. Subir imagen a ECR
2. Crear Task Definition en ECS
3. Crear servicio Fargate
4. Configurar Load Balancer
```

### Subir imagen a ECR

```bash
# Autenticarse en ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com

# Crear repositorio
aws ecr create-repository --repository-name ai-engineer-api

# Taggear y subir imagen
docker tag ai-enginner-api:latest <account>.dkr.ecr.us-east-1.amazonaws.com/ai-engineer-api:latest
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/ai-engineer-api:latest
```

---

## Monitoreo en producción

| Herramienta | Para qué |
|---|---|
| `GET /health` | Verificar que la API está viva |
| AWS CloudWatch | Logs y métricas en la nube |
| Docker logs | Logs locales del contenedor |

---

## Checklist de producción

- ✅ API con `/health` endpoint
- ✅ Manejo de errores con HTTPException
- ✅ Validación de datos con Pydantic
- ✅ Dockerfile optimizado
- ✅ `.dockerignore` configurado
- ⬜ Variables de entorno para secrets
- ⬜ HTTPS configurado
- ⬜ Rate limiting
- ⬜ Autenticación

---

## Archivos

| Archivo | Descripción |
|---|---|
| `Dockerfile` | Definición de la imagen |
| `.dockerignore` | Archivos excluidos de la imagen |
| `requirements.txt` | Dependencias del proyecto |
| `python/fase5/main.py` | API FastAPI con FAISS |
