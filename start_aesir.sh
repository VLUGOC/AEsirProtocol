#!/usr/bin/env bash
cd "$(dirname "$0")"

# Carga variables del .env
set -a
[ -f .env ] && source .env
set +a

# Activa entorno virtual
source env/bin/activate

# Inicia backend con logs
exec uvicorn api.server:app --host 0.0.0.0 --port 8000 --reload
