#!/usr/bin/env python3
"""
Priority Agent v0.1
Escucha una orden y prioriza tareas según urgencia.
"""

import sys
from datetime import datetime

LOG_FILE = "engineer/logs/priority.log"

def log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def prioritize(task: str) -> str:
    if "error" in task.lower():
        return "⚠️ ALTA PRIORIDAD – Necesita reparación inmediata."
    elif "mejora" in task.lower():
        return "📈 MEDIA PRIORIDAD – Optimización sugerida."
    else:
        return "📌 BAJA PRIORIDAD – Puede esperar."

if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "SIN TAREA"
    result = prioritize(task)
    log(f"Tarea: {task} => {result}")
    print(result)
