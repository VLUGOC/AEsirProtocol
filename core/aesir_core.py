import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel

console = Console()
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    console.print("[bold red]ERROR:[/bold red] No se encontró OPENAI_API_KEY en el archivo .env")
    raise SystemExit(1)

client = OpenAI(api_key=api_key)

def aesir_chat(prompt):
    """
    Envía una consulta al modelo ChatGPT (núcleo de razonamiento AEsir)
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"[AEsir Protocol] Orquestador: {prompt}"
    )
    return response.output[0].content[0].text

def main():
    console.print(Panel.fit(
        "[bold cyan]🧠 AEsir Protocol v1.0[/bold cyan]\n"
        "[green]Conectado a ChatGPT (núcleo Stark AI)[/green]\n"
        "Escribe 'salir' para finalizar.",
        border_style="cyan"
    ))

    while True:
        prompt = console.input("[bold yellow]Tú:[/bold yellow] ").strip()
        if prompt.lower() in ["salir", "exit", "quit"]:
            console.print("[bold magenta]Cerrando AEsir Core...[/bold magenta]")
            break

        try:
            answer = aesir_chat(prompt)
            console.print(Panel(answer, title="AEsir", border_style="magenta"))
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
