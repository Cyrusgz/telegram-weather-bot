import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot activo"

def run_flask():
    app_web.run(host='0.0.0.0', port=8080)

def start_flask():
    thread = threading.Thread(target=run_flask)
    thread.start()

def icono_clima(desc: str) -> str:
    desc = desc.lower()
    if "lluv" in desc:
        return "🌧️"
    elif "nublado" in desc or "nubes" in desc:
        return "☁️"
    elif "sol" in desc or "claro" in desc or "despejado" in desc:
        return "☀️"
    elif "nieve" in desc:
        return "❄️"
    elif "tormenta" in desc:
        return "⛈️"
    return "🌤️"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy tu bot del clima.\n"
        "Usa /clima <ciudad> para saber el tiempo.\n"
        "Ejemplo: /clima Vigo\n"
        "Usa /help para ayuda."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos:\n"
        "/start - Mensaje de bienvenida\n"
        "/clima <ciudad> - Muestra el clima actual de la ciudad\n"
        "/help - Muestra esta ayuda"
    )

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, escribe una ciudad. Ejemplo: /clima Vigo")
        return
    
    ciudad = " ".join(context.args)
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={ciudad}&appid={WEATHER_API_KEY}&units=metric&lang=es"
    )

    res = requests.get(url).json()
    
    if res.get("cod") != 200:
        await update.message.reply_text("Ciudad no encontrada. Prueba otra.")
        return

    temp = res["main"]["temp"]
    humedad = res["main"]["humidity"]
    viento = res["wind"]["speed"]
    desc = res["weather"][0]["description"]
    emoji = icono_clima(desc)

    mensaje = (
        f"{emoji} Clima en *{ciudad.title()}*:\n"
        f"Descripción: {desc.capitalize()}\n"
        f"Temperatura: {temp}°C\n"
        f"Humedad: {humedad}%\n"
        f"Viento: {viento} m/s"
    )

    await update.message.reply_markdown(mensaje)

if __name__ == '__main__':
    start_flask()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("clima", clima))
    app.run_polling()
