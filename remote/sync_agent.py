import os
import subprocess
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI(
    title="AEsir Sync Agent",
    description="Agente para escribir archivos y ejecutar comandos de forma segura en AEsirProtocol",
    version="0.1"
)

# Token de autenticación
AUTH_TOKEN = os.getenv("AESIR_TOKEN", "CAMBIA_ESTE_TOKEN")

# Comandos permitidos
ALLOWED_COMMANDS = [
    "mkdir",
    "ls",
    "cat",
    "python",
    "pip",
    "git",
    "mv",
    "cp",
    "rm",
    "echo"
]


def is_safe_command(cmd: str) -> bool:
    return any(cmd.startswith(prefix) for prefix in ALLOWED_COMMANDS)


def ensure_parent_dir(path: str):
    parent = os.path.dirname(path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)


@app.post("/write_file")
async def write_file(request: Request):
    """
    Crea o sobrescribe un archivo dentro de AEsirProtocol.
    Body JSON:
    {
      "token": "...",
      "relative_path": "modules/nasa/client.py",
      "content": "...."
    }
    """
    body = await request.json()
    token = body.get("token")
    rel_path = body.get("relative_path")
    content = body.get("content")

    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

    if not rel_path or not isinstance(rel_path, str):
        raise HTTPException(status_code=400, detail="relative_path inválido")

    base_dir = os.path.abspath(os.path.dirname(_file_) + "/..")
    abs_path = os.path.abspath(os.path.join(base_dir, rel_path))

    # Seguridad básica: el archivo debe estar dentro de AEsirProtocol
    if not abs_path.startswith(base_dir):
        raise HTTPException(status_code=403, detail="Ruta fuera del proyecto")

    ensure_parent_dir(abs_path)

    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)

    timestamp = datetime.now().isoformat()

    return {
        "status": "ok",
        "action": "write_file",
        "relative_path": rel_path,
        "abs_path": abs_path,
        "timestamp": timestamp
    }


@app.post("/run")
async def run_command(request: Request):
    """
    Ejecuta un comando permitido.
    Body JSON:
    {
      "token": "...",
      "cmd": "ls modules"
    }
    """
    body = await request.json()
    token = body.get("token")
    cmd: Optional[str] = body.get("cmd")

    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

    if not cmd:
        raise HTTPException(status_code=400, detail="cmd requerido")

    if not is_safe_command(cmd):
        raise HTTPException(status_code=403, detail=f"Comando no permitido: {cmd}")

    timestamp = datetime.now().isoformat()

    try:
        output = subprocess.check_output(
            cmd,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    return {
        "status": "ok",
        "action": "run",
        "cmd": cmd,
        "output": output,
        "timestamp": timestamp
    }


if _name_ == "_main_":
    # Escucha en todas las interfaces, puerto 9100
    uvicorn.run(app, host="0.0.0.0", port=9100)
