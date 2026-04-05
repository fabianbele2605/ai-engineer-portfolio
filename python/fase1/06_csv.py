import csv

def lee_csv(ruta):
    estudiantes = []
    with open(ruta, "r") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            estudiantes.append({
                "nombre": fila["nombre"],
                "horas": int(fila["horas_estudio"]),
                "fase": int(fila["fase_actual"])
            })
    return estudiantes

def promedio_horas(estudiantes):
    total = sum(e["horas"] for e in estudiantes)
    return total / len(estudiantes)

estudiantes = lee_csv("matematicas/datos.csv")

for e in estudiantes:
    print(f"{e['nombre']} | Fase {e['fase']} | {e['horas']}h/día")

print(f"\nPromedio de estudio: {promedio_horas(estudiantes):.1f}h/día")
