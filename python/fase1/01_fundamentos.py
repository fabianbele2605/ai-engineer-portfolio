# Variables y tipos de datos
nombre = "IA Engineer"
version = 3.12
activo = True


print(f"Hola, futuro {nombre}!")
print(f"Python version: {version}")
print(f"Entorno activo: {activo}")

# Lista
habilidades = ["Python", "ML", "LLMs", "Rust"]
for skill in habilidades:
    print(f"- {skill}")


# Diccionario -> clave:valor (como un JSON)
perfil = {
    "nombre": "Fabian",
    "rol": "AI Engineer",
    "nivel": 1
}

print(f"\nPerfil: {perfil['nombre']} - {perfil['rol']} - {perfil['nivel']}")

# Subir de nivel
perfil["nivel"] += 1
print(f"Subiste de nivel! Ahora eres nivel {perfil['nivel']}")