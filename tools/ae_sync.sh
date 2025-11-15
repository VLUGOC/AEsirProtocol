#!/bin/bash

# IP del TELÉFONO a través de Tailscale o WiFi
PHONE_IP="100.111.107.73"        # <- esta es la IP del móvil en Tailscale que vimos
PHONE_USER="u0_a336"             # <- este es tu usuario de Termux (compruébalo con whoami en el móvil)
PHONE_PATH="/data/data/com.termux/files/home/"   # raíz del HOME de Termux

# Carpeta destino en tu PC
PC_PATH="/home/victor/AEsirProtocol/phone_sync/"

echo "🔄 Iniciando sincronización desde $PHONE_USER@$PHONE_IP ..."
rsync -avzP \
  -e "ssh -p 8022" \
  ${PHONE_USER}@${PHONE_IP}:${PHONE_PATH} \
  ${PC_PATH}

echo "✅ Sincronización completada."
