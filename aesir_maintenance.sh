#!/bin/bash

LOG=/home/victor/AEsirProtocol/maintenance.log

echo "────────── $(date) ──────────" >> $LOG
echo "[AEsir] Starting maintenance..." >> $LOG

# Actualizaciones
sudo apt update -y >> $LOG 2>&1
sudo apt upgrade -y >> $LOG 2>&1
sudo apt autoremove -y >> $LOG 2>&1
sudo apt autoclean -y >> $LOG 2>&1

# Optimización
rm -rf ~/.cache/* >> $LOG 2>&1
journalctl --vacuum-time=3d >> $LOG 2>&1

# Revisar servicios
systemctl --failed >> $LOG 2>&1

echo "[AEsir] Maintenance complete." >> $LOG
echo "" >> $LOG
