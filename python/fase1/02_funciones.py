def saludar(nombre, rol="AI Engineer"):
    return f"Hola {nombre}, eres un {rol}"

def calcular_progreso(fase_actual, total_fases=6):
    porcentaje = (fase_actual / total_fases) * 100
    return f"Progreso: {porcentaje:.1f}%"

print(saludar("Fabian"))
print(saludar("Fabian", "ML Engineer"))
print(calcular_progreso(1))