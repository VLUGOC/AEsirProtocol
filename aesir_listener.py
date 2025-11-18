#!/usr/bin/env python3
import socket
import subprocess
import os

HOST = "0.0.0.0"
PORT = 9001


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    print(f"[AEsir] Listener activo en {HOST}:{PORT}", flush=True)

    while True:
        conn, addr = s.accept()
        print(f"[AEsir] Conexión desde {addr}", flush=True)

        data = conn.recv(4096).decode().strip()

        if not data:
            conn.send(b"ERR: empty\n")
            conn.close()
            continue

        print(f"[AEsir] Ejecutando: {data}", flush=True)

        try:
            subprocess.Popen(
                data,
                shell=True,
                env={
                    **os.environ,
                    "DISPLAY": ":0",
                    "XAUTHORITY": "/home/victor/.Xauthority",
                }
            )
            conn.send(b"OK\n")
        except Exception as e:
            conn.send(f"ERR: {str(e)}\n".encode())

        conn.close()


if __name__ == "__main__":
    main()
