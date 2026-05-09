import os
import json
import datetime


HISTORIAL_DIR = "data"
os.makedirs(HISTORIAL_DIR, exist_ok=True)

def ruta_historial():
    return os.path.join(HISTORIAL_DIR, "historial.json")

def cargar_historial():
    ruta = ruta_historial()

    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def guardar_historial(accion, receta):
    historial = cargar_historial()

    entrada = {
        "accion" : accion,
        "receta" : receta,
        "timestamp" : datetime.datetime.now().isoformat()
    }

    historial.append(entrada)

    try:
        with open(ruta_historial(), "w", encoding="utf-8") as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error al guardar historial: {e}")