[7:39 AM, 11/16/2025] Victor Lugo: from pathlib import Path
from typing import Dict, Any, List

class CodeGen:
    def _init_(self, base_dir: Path):
        self.base_dir = base_dir

    def build(self, plan) -> Dict[str, Any]:
        if plan.action == "create_agent":
            return self._build_agent(plan)

        return {"status": "error", "artifacts": [], "reason": f"Acción desconocida {plan.action}"}

    def _build_agent(self, plan) -> Dict[str, Any]:
        agent_name = "auto_agent"
        path = f"engineer/agents/{agent_name}.py"

        code = f'''"""
Agente generado automáticamente.
Intent: {plan.intent}
"""

class AutoAgent:
    def run(self):
        print("Ejecutando agente con intención:")
        print({plan.intent!r})
'''

        return {
            "status": "success…
[7:41 AM, 11/16/2025] Victor Lugo: nano engineer/core/validator.py
[7:41 AM, 11/16/2025] Victor Lugo: import ast

class Validator:
    def check(self, output):
        for art in output.get("artifacts", []):
            if art["type"] == "file" and art["path"].endswith(".py"):
                try:
                    ast.parse(art["content"])
                except SyntaxError as e:
                    return {"status": "error", "reason": f"Error en {art['path']}: {e}"}
        return output
[7:41 AM, 11/16/2025] Victor Lugo: python3 engineer/engineer_cli.py "crear agente que revise errores"
[7:42 AM, 11/16/2025] Victor Lugo: victor@AEsir-Protocol:~/AEsirProtocol$ python3 engineer/engineer_cli.py "crear agente que revise errores"
Traceback (most recent call last):
  File "/home/victor/AEsirProtocol/engineer/engineer_cli.py", line 6, in <module>
    ROOT = Path(file).resolve().parent.parent
                ^^^^^^
NameError: name 'file' is not defined. Did you mean: '_file_'?
victor@AEsir-Protocol:~/AEsirProtocol$
[7:42 AM, 11/16/2025] Victor Lugo: nano engineer/engineer_cli.py
[7:46 AM, 11/16/2025] Victor Lugo: victor@AEsir-Protocol:~/AEsirProtocol$ python3 engineer/engineer_cli.py "crear agente que revise errores"
Traceback (most recent call last):
  File "/home/victor/AEsirProtocol/engineer/engineer_cli.py", line 6, in <module>
    ROOT = Path(file).resolve().parent.parent
                ^^^^^^
NameError: name 'file' is not defined. Did you mean: '_file_'?
victor@AEsir-Protocol:~/AEsirProtocol$ nano engineer/engineer_cli.py
victor@AEsir-Protocol:~/AEsirProtocol$ ython3 engineer/engineer_cli.py "crear agente que revise errores"
Orden «ython3» no encontrada. Quizá quiso decir:
  la orden «python3» del paquete deb «python3 (3.12.3-0ubuntu2.1)»
  la orden «cython3» del paquete deb «cython3 (3.0.7-2ubuntu1)»
  la orden «cython3» del paquete deb «cython3-legacy (0.29.…
[7:48 AM, 11/16/2025] Victor Lugo: systemctl status aesir-listener
[7:48 AM, 11/16/2025] Victor Lugo: sudo systemctl restart aesir-listener
[7:49 AM, 11/16/2025] Victor Lugo: sudo ss -tulpn | grep 9001
[7:50 AM, 11/16/2025] Victor Lugo: sudo journalctl -u aesir-listener -n 50 --no-pager
[7:51 AM, 11/16/2025] Victor Lugo: victor@AEsir-Protocol:~$ sudo journalctl -u aesir-listener -n 50 --no-pager
nov 14 17:46:20 AEsir-Protocol python3[501984]:     conn.send(b"ERR: Comando vacío\n")
nov 14 17:46:20 AEsir-Protocol python3[501984]:               ^^^^^^^^^^^^^^^^^^^^^^^
nov 14 17:46:20 AEsir-Protocol python3[501984]: SyntaxError: bytes can only contain ASCII literal characters
nov 14 17:46:20 AEsir-Protocol systemd[1]: aesir-listener.service: Main process exited, code=exited, status=1/FAILURE
nov 14 17:46:20 AEsir-Protocol systemd[1]: aesir-listener.service: Failed with result 'exit-code'.
nov 14 17:46:20 AEsir-Protocol systemd[1]: aesir-listener.service: Scheduled restart job, restart counter is at 2.
nov 14 17:46:20 AEsir-Protocol systemd[1]: Started aesir-listener.service - AE…
[7:52 AM, 11/16/2025] Victor Lugo: nano ~/AEsirProtocol/aesir_listener.py
[7:54 AM, 11/16/2025] Victor Lugo: #!/usr/bin/env python3
import socket
import subprocess
import sys

HOST = "0.0.0.0"
PORT = 9091

def run_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        if result.stdout.strip() == "" and result.stderr.strip() == "":
            return "OK\n"
        if result.stdout.strip() != "":
            return result.stdout
        return "ERR\n" + result.stderr
    except Exception as e:
        return f"ERR\n{e}\n"

def main():
    print("[AEsir Listener] Starting server...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)

        print(f"[AEsir Listener] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            print(f"[AEsir Listener] Connection from {addr}")

            with conn:
                data = conn.recv(4096).decode("utf-8").strip()

                if not data:
                    conn.send("ERR: Empty command\n".encode("utf-8"))
                    continue

                print(f"[AEsir Listener] Running command: {data}")

                output = run_command(data)

                try:
                    conn.send(output.encode("utf-8", errors="replace"))
                except:
                    conn.send("ERR: Failed to send output\n".encode("utf-8"))

if _name_ == "_main_":
    main()
