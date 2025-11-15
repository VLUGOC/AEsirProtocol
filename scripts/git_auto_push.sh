#!/bin/bash

REPO_DIR="/home/victor/AEsirProtocol"
LOG_FILE="$REPO_DIR/github_autopush.log"
DATE=$(date "+%Y-%m-%d %H:%M:%S")

cd "$REPO_DIR" || exit

# Check for changes
if git status --porcelain | grep -q .; then
    echo "[$DATE] Cambios detectados. Realizando push..." >> "$LOG_FILE"
    git add .
    git commit -m "Auto-sync: $DATE"
    git push origin main >> "$LOG_FILE" 2>&1

    echo "[$DATE] Push completado." >> "$LOG_FILE"
else
    echo "[$DATE] Sin cambios. Nada que enviar." >> "$LOG_FILE"
fi
