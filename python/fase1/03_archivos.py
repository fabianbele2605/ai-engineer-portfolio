import json

# Escribir JSON
datos = {
    "estudiante": "Fabian",
    "fase": 1,
    "temas": ["variable", "funciones", "archivos"]
}

with open("python/progreso.json", "w") as f:
    json.dump(datos, f, indent=2)

print("Archivo guardado!")

# Leer JSON
with open("python/progreso.json", "r") as f:
    cargado = json.load(f)

print(f"Estudiante: {cargado['estudiante']}")
print(f"Temas aprendidos: {cargado['temas']}")