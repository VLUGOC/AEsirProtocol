#!/usr/bin/env python3
"""
Safe executor – recibe el prompt desde termux,
lo manda a agentes según prioridad y guarda historial.
"""

import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("/home/victor/AEsirProtocol/brain_logs").resolve()

def save_log(prompt, output):
    LOG_PATH.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(LOG_PATH / f"{ts}.log", "w") as f:
        f.write(f"PROMPT: {prompt}\n")
        f.write(f"OUTPUT: {output}\n")

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "NO_PROMPT"
    output = f"Ejecutado: {prompt}"

    # aquí se puede llamar a otros agentes
    save_log(prompt, output)
    print(output)
