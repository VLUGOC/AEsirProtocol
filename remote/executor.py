import os
import subprocess
from datetime import datetime

from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI(title="AEsir Remote Executor", version="0.1")

AUTH_TOKEN = os.getenv("AESIR_TOKEN", "CAMBIA_ESTE_TOKEN")

ALLOWED_COMMANDS = [
    "mkdir",
    "touch",
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


def is_safe(cmd: str) -> bool:
    return any(cmd.startswith(allowed) for allowed in ALLOWED_COMMANDS)


@app.post("/execute")
async def execute(request: Request):
    body = await request.json()
    token = body.get("token")
    cmd = body.get("cmd")

    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

    if not is_safe(cmd):
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
        "timestamp": timestamp,
        "executed": cmd,
        "output": output
    }


if _name_ == "_main_":
    uvicorn.run(app, host="0.0.0.0", port=9000)
