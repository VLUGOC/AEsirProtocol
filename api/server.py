from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os, traceback

app = FastAPI(title="AEsirProtocol Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "AEsir backend running"}

@app.post("/jarvis")
async def jarvis(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        if not prompt:
            return {"error": "Prompt vacío"}

        # Modelos posibles: "gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
        )
        reply = response.choices[0].message.content
        return {"reply": reply}

    except Exception as e:
        print("\n[ERROR] Fallo en /jarvis:")
        traceback.print_exc()
        return {"error": str(e)}
