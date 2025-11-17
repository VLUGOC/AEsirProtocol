#!/usr/bin/env python3
"""
Engineer v0.1
Capa central que orquesta: planner -> codegen -> validator.
"""

import json
from pathlib import Path

from engineer.core.planner import Planner
from engineer.core.codegen import CodeGen
from engineer.core.validator import Validator


PROJECT_ROOT = Path(_file_).resolve().parent.parent


def run_engineer(task: dict) -> dict:
    """
    task: dict con al menos:
      {
        "task_id": "opcional",
        "user_intent": "texto natural de la orden",
        "context": {...}
      }
    """
    planner = Planner()
    plan = planner.build_plan(task)

    generator = CodeGen(base_dir=PROJECT_ROOT / "engineer")
    output = generator.build(plan)

    validator = Validator()
    checked = validator.check(output)

    # Si hay artifacts tipo "file", escribirlos a disco
    for art in checked.get("artifacts", []):
        if art.get("type") == "file":
            file_path = PROJECT_ROOT / art["path"]
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(art["content"], encoding="utf-8")
            art["abs_path"] = str(file_path)

    return checked
