#!/bin/bash

# IP del teléfono con ADB en modo TCP
PHONE_IP="192.168.20.133:5555"

echo "🔗 AEsir Linker iniciado..."
echo "Conectando a $PHONE_IP"

adb connect "$PHONE_IP" >/dev/null 2>&1

while true; do
    if [ -f command.sh ]; then
        CMD=$(cat command.sh)
        echo "📤 Enviando comando al teléfono: $CMD"
        adb shell "$CMD" > output.txt 2>&1
        echo "📥 Respuesta guardada en output.txt"
        rm command.sh
    fi
    sleep 1
done
