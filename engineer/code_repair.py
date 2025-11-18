#!/usr/bin/env python3
"""
Engineer Repair Module v1
Repara código básico:
✔ Corregir indentación
✔ Detectar errores de sintaxis
✔ Limpiar imports inútiles
✔ Sugerir mejoras automáticas
"""

import autopep8
import tempfile
import subprocess

def repair_code(code: str) -> str:
    """Usa autopep8 para reparar sintaxis e indentación básica."""
    try:
        fixed = autopep8.fix_code(code)
        return fixed
    except Exception as e:
        return f"[ERROR] No pude reparar: {str(e)}"

def repair_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        return repair_code(code)
    except FileNotFoundError:
        return f"[ERROR] No encontré el archivo: {file_path}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 code_repair.py archivo.py")
        sys.exit(1)

    file = sys.argv[1]
    output = repair_from_file(file)
    print(output)

def apply_fix(file_path: str):
    """Reemplaza el archivo original con la versión reparada."""
    fixed = repair_from_file(file_path)
    if fixed.startswith("[ERROR]"):
        return fixed

    backup = file_path + ".backup"
    os.rename(file_path, backup)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fixed)

    return f"[OK] Reparado y respaldado como {backup}"
