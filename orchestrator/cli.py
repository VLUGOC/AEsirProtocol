# orchestrator/cli.py
import os
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
import json
from datetime import datetime
from pathlib import Path

# === Inicialización del entorno ===
load_dotenv()
console = Console()

# === Variables del sistema ===
api_key = os.getenv("OPENAI_API_KEY")
orchestrator = os.getenv("ORCHESTRATOR_NAME", "Victor")
jarvis_name = os.getenv("JARVIS_NAME", "Jarvis")

client = OpenAI(api_key=api_key)

# === Memoria temporal ===
MEMORY_FILE = Path("data/memory/journal.jsonl")
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_to_memory(prompt, answer):
    """Guarda cada interacción local en memoria."""
    entry = {
        "time": str(datetime.now()),
        "user": prompt,
        "response": answer
    }
    with open(MEMORY_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")

# === Núcleo del razonamiento AEsir (Jarvis) ===
def aesir_chat(prompt):
    """
    Envía una consulta al modelo ChatGPT (núcleo AEsir)
    """
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"[{jarvis_name}] {orchestrator}: {prompt}"
        )
        answer = response.output[0].content[0].text
        save_to_memory(prompt, answer)
        return answer
    except Exception as e:
        return f"Error al procesar la solicitud: {e}"

# === Interfaz principal ===
def main():
    console.print(Panel.fit(
        f"[bold cyan]🧠 AEsir Protocol v1.0[/bold cyan]\n"
        f"[green]Conectado a {jarvis_name} (núcleo Stark AI)[/green]\n"
        "Escribe 'salir' para finalizar.",
        border_style="cyan"
    ))

    while True:
        prompt = console.input("[bold yellow]Tú:[/bold yellow] ").strip()
        if prompt.lower() in ["salir", "exit", "quit"]:
            console.print("[bold magenta]Cerrando AEsir Core...[/bold magenta]")
            break

        answer = aesir_chat(prompt)
        console.print(Panel(answer, title=jarvis_name, border_style="magenta"))

if __name__ == "__main__":
    main()
