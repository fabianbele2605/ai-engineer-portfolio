import json
import os

ARCHIVO = "python/mi_progreso.json"

def cargar_progreso():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {"nombre": "Fabian", "fase": 1, "temas": []}

def guardar_progreso(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=2)

def agregar_tema(datos, tema):
    if tema not in datos["temas"]:
        datos["temas"].append(tema)
        guardar_progreso(datos)
        print(f"✅ '{tema}' agregado!")
    else:
        print(f"⚠️ '{tema}' ya estaba registrado")

def mostrar_progreso(datos):
    print(f"\n👤 {datos['nombre']} | Fase {datos['fase']}/6")
    print(f"📚 Temas aprendidos ({len(datos['temas'])})")
    for t in datos["temas"]:
        print(f"  - {t}")

# Programa principal
progreso = cargar_progreso()
agregar_tema(progreso, "variables")
agregar_tema(progreso, "funciones")
agregar_tema(progreso, "archivos")
agregar_tema(progreso, "clases")
agregar_tema(progreso, "clases")  # duplicado intencional
mostrar_progreso(progreso)