from pathlib import Path
from typing import Dict, Any, List

class CodeGen:
    def _init_(self, base_dir: Path):
        self.base_dir = base_dir

    def build(self, plan) -> Dict[str, Any]:
        if plan.action == "create_agent":
            return self._build_agent(plan)

        return {"status": "error", "artifacts": [], "reason": f"Acción desconocida {plan.action}"}

    def _build_agent(self, plan) -> Dict[str, Any]:
        agent_name = "auto_agent"
        path = f"engineer/agents/{agent_name}.py"

        code = f'''"""
Agente generado automáticamente.
Intent: {plan.intent}
"""

class AutoAgent:
    def run(self):
        print("Ejecutando agente con intención:")
        print({plan.intent!r})
'''

        return {
            "status": "success",
            "artifacts": [{
                "type": "file",
                "path": path,
                "content": code
            }],
            "meta": {"agent": agent_name}
        }
