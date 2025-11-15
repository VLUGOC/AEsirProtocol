#!/bin/bash

PORT=8022
CMD_FILE="$HOME/AEsirProtocol/linux_bridge/command.txt"
OUT_FILE="$HOME/AEsirProtocol/linux_bridge/output.txt"

echo "🔗 AEsir Linux Listener iniciado en puerto $PORT..."
echo "Esperando comandos desde el teléfono..."

while true; do
    # Escucha un comando
    nc -l -p $PORT > "$CMD_FILE"

    CMD=$(cat "$CMD_FILE")
    echo ">> Ejecutando: $CMD"

    bash -c "$CMD" &> "$OUT_FILE"

    echo "OK" > "$OUT_FILE"
done
