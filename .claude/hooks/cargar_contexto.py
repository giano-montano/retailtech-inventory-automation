#!/usr/bin/env python3
"""Hook SessionStart — inyecta estado de datos + reglas de negocio en el contexto.

Salida (stdout): UN ÚNICO objeto JSON con hookSpecificOutput.additionalContext.
Cualquier mensaje informativo se escribe en stderr para no contaminar la salida.
"""
import csv
import json
import os
import sys
from datetime import datetime

# Raíz del proyecto: .claude/hooks/cargar_contexto.py -> tres niveles arriba.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(ROOT, "data")

DATA_FILES = [
    "inventario.csv",
    "ventas.csv",
    "proveedores.csv",
    "ordenes.csv",
    "inventario_muestra.csv",
]


def header_and_row_count(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [], 0
        n = sum(1 for _ in reader)
    return header, n


def main():
    lines = []
    lines.append("CONTEXTO RetailTech — cargado automáticamente al inicio de sesión.")
    lines.append("")
    lines.append("## Estado de datos (data/)")

    for name in DATA_FILES:
        path = os.path.join(DATA_DIR, name)
        if not os.path.exists(path):
            lines.append(f"- {name}: NO ENCONTRADO")
            continue
        try:
            header, n = header_and_row_count(path)
        except Exception as exc:  # noqa: BLE001
            lines.append(f"- {name}: ERROR al leer ({exc})")
            continue
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")
        lines.append(f"- {name}: {n} filas · modificado {mtime}")
        lines.append(f"  columnas: {', '.join(header)}")

    lines.append("")
    lines.append("## Reglas de negocio (recordatorio)")
    lines.append("- Stock mínimo = 20% de la venta mensual promedio.")
    lines.append("  Producto bajo mínimo si: stock_actual < 0.2 × ventas_promedio_mensual.")
    lines.append("- Lead time de proveedores: 7–21 días según categoría.")
    lines.append("- Clasificación ABC por valor de inventario: A > 70% del valor; B entre 20% y 70%; C < 20%.")
    lines.append("- Frecuencia de revisión: A diario; B y C semanal.")
    lines.append("- Reconciliación: discrepancia > 2% entre fuentes = significativa (reportar).")
    lines.append("- Restricciones: no modificar data/; salidas en output/; alertas de email simuladas con .log;")
    lines.append("  no inventar información ausente; distinguir datos observados de recomendaciones.")

    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n".join(lines),
        }
    }
    # ensure_ascii=True (default) -> salida ASCII pura, inmune a diferencias de
    # codificación de stdout entre Windows/bash/PowerShell. El parser JSON del
    # harness decodifica los escapes \uXXXX correctamente.
    sys.stdout.write(json.dumps(payload, ensure_ascii=True))


if __name__ == "__main__":
    main()
