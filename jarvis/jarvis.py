import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client =
OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    try:
      command =
 recognizer.recognize_google(audio, language= "es-ES")
    print(f"*brain* You said:{command}")
    retunr command.lower()
   except sr.UnknownValueError:
    speak("No te entendi, repite por favor.")
    return ""

def ask_openai(prompt):
   response = cliente.chat.completionsimport os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="es-ES")
            print(f"🧠 You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("No te entendí, repite por favor.")
            return ""

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Eres Jarvis, un asistente personal leal e inteligente."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

while True:
    speak("Estoy listo, Victor.")
    command = listen()
    if "detente" in command or "adiós" in command:
        speak("Hasta luego, señor.")
        break
    elif command:
        reply = ask_openai(command)
        print("🤖 Jarvis:", reply)
        speak(reply)
