#!/usr/bin/env python3
import os
import glob

LOG_DIR = "/home/victor/AEsirProtocol/brain_logs"

def find_latest_log():
    files = glob.glob(os.path.join(LOG_DIR, "*.log"))
    if not files:
        return None
    return max(files, key=os.path.getctime)

def analyze(log_path):
    with open(log_path, "r") as f:
        content = f.read()

    content_lower = content.lower()

    if "docker" in content_lower:
        return "investigar comandos para docker-compose y agente"
    elif "error" in content_lower:
        return "analizar error y buscar solución"
    else:
        return "seguir con el diseño modular de agentes"

if __name__ == "__main__":
    log = find_latest_log()
    if not log:
        print("No hay logs")
        exit(0)

    conclusion = analyze(log)
    print(f"CHATGPT_SUGGESTION: {conclusion}")
