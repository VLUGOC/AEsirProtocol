#!/usr/bin/env python3
import socket, subprocess, os

HOST = "0.0.0.0"
PORT = 8022

print("[AEsir] Listener activo en {}:{}".format(HOST, PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("[AEsir] Conexión desde", addr)

    data = conn.recv(4096).decode().strip()

    if not data:
        print("[AEsir] Comando vacío ignorado.")
        conn.send("ERR: empty\n".encode())
        conn.close()
        continue

    print("[AEsir] Ejecutando:", data)

    try:
        result = subprocess.Popen(
            data,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={
                **os.environ,
                "DISPLAY": ":0.0",
                "XAUTHORITY": "/home/victor/.Xauthority",
            }
        )

        out, err = result.communicate(timeout=5)

        response = (out + err).decode(errors="ignore")
        if not response:
            response = "OK\n"

        conn.send(response.encode())

    except Exception as e:
        conn.send(("ERR: {}\n".format(e)).encode())

    conn.close()
