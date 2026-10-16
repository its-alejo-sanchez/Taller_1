from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(BASE_DIR / "biblioteca"))

import Libreria

print(Libreria.velocidad(12, 3))

ruta = BASE_DIR / "datos" / "mediciones.csv"
