from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Plan:
    action: str
    intent: str
    params: Dict[str, Any]

class Planner:
    def build_plan(self, task: Dict[str, Any]) -> Plan:
        intent = task.get("user_intent", "").lower()

        if "crear agente" in intent or "nuevo agente" in intent:
            action = "create_agent"
        else:
            action = "unknown"

        return Plan(action, task["user_intent"], {"raw": task})

