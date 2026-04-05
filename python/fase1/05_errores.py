import json

def leer_json(ruta):
    try:
        with open(ruta, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Archivo '{ruta}' no encontrado")
    except json.JSONDecodeError:
        print(f"❌ El archivo '{ruta}' no es JSON valido")
    return None

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("❌ No se puede dividir entre cero")
        return None
    
# Prueba
print(leer_json("python/mi_progreso.json"))     # existe ✅
print(leer_json("python/no_existe.json"))       # no existe ❌
print(dividir(10, 2))                           # ok ✅
print(dividir(10, 0))                           # error ❌