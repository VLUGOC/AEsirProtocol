#!/usr/bin/env python3

import json, sys
from pathlib import Path

ROOT = Path(___file___).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engineer.run_engineer import run_engineer

def main():
    if not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
        try:
            task = json.loads(raw)
        except:
            print("STDIN inválido")
            sys.exit(1)
    else:
        if len(sys.argv) < 2:
            print("Uso: engineer_cli.py \"tarea\"")
            sys.exit(1)
        task = {
            "task_id": "manual",
            "user_intent": " ".join(sys.argv[1:]),
            "context": {}
        }

    result = run_engineer(task)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if _name_ == "_main_":
    main()
