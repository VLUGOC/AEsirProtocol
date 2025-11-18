#!/usr/bin/env python3
"""
ENGINEER v1.2
Base sólida y lista para crecer:
✔ Lee archivos del proyecto
✔ Analiza y loguea resultados
✔ Facilita integrar IA después
"""

import os
import sys
from pathlib import Path

# ==============================
# CONFIGURACIÓN
# ==============================
PROJECT_ROOT = Path(_file_).resolve().parent.parent
LOG_FILE = PROJECT_ROOT / "engineer" / "logs" / "engineer.log"


def log(message: str):
    """Escribe mensajes en log del ingeniero."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def load_file_context(file_path: str) -> str:
    """Lee contenido del archivo si existe."""
    full_path = PROJECT_ROOT / file_path
    if not full_path.exists():
        return f"[ERROR] No encontré el archivo: {full_path}"
    
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()


def analyze_code(prompt: str, context: str) -> str:
    """Simula análisis. Aquí conectaremos IA después."""
    return f"""
=== ANALISIS DEL INGENIERO ===
🧠 Prompt recibido: {prompt}

📄 Fragmento del archivo:
{context[:600]}

🔍 Conclusión (versión 1.2):
- Código cargado exitosamente
- Se pueden detectar funciones, clases y errores básicos
- Se puede generar plan de mejora
- Listo para integrar reparador automático

🧩 Siguiente paso recomendado:
=> Crear módulo: code_repair.py
=> Añadir agente de validación
    """.strip()


def run_engineer(prompt: str, file_to_read: str):
    """Core del sistema ingeniero."""
    log(f"[RUN] Prompt: {prompt} | Archivo: {file_to_read}")
    
    context = load_file_context(file_to_read)
    result = analyze_code(prompt, context)
    
    print(result)
    log(result)


# ==============================
# MAIN
# ==============================
if _name_ == "_main_":
    if len(sys.argv) < 2:
        print("Uso: python3 engineer/run_engineer.py \"mi pregunta\" [archivo]")
        sys.exit(1)

    prompt = sys.argv[1]
    file_to_read = sys.argv[2] if len(sys.argv) > 2 else "aesir_listener.py"
    run_engineer(prompt, file_to_read)
