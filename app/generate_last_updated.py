import subprocess
import json
from pathlib import Path


import subprocess
from datetime import datetime

def get_last_updated_date():
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=iso"],
            capture_output=True,
            text=True,
            check=True,
        )
        full_date = result.stdout.strip()
        dt = datetime.fromisoformat(full_date)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Falló al obtener la fecha del último commit: {e}")
    except FileNotFoundError:
        print("[Error] Git no está instalado o no está disponible.")
    except Exception as e:
        print(f"[Error] Error inesperado al procesar la fecha: {e}")

    return "Fecha no disponible"



if __name__ == "__main__":
    date = get_last_updated_date()

    # Asegura que el directorio exista
    data_dir = Path("app/data")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Escribe el archivo
    output_path = data_dir / "last_updated.json"
    with open(output_path, "w") as f:
        json.dump({"last_updated": date}, f)

    print(f"✅ Archivo generado en: {output_path} con fecha: {date}")
