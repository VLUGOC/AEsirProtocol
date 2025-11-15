#!/usr/bin/env python3
import socket, subprocess, os

HOST = "0.0.0.0"
PORT = 8022

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

os.environ["DISPLAY"] = ":0.0"
os.environ["XAUTHORITY"] = "/home/victor/.Xauthority"

print("FAST BRIDGE ACTIVE:", HOST, PORT)

while True:
    conn, addr = s.accept()
    cmd = conn.recv(4096).decode().strip()

    if not cmd:
        conn.close()
        continue

    try:
        out = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT
        )
        conn.send(out)
    except subprocess.CalledProcessError as e:
        conn.send(e.output)

    conn.close()
