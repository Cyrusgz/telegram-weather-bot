# Bot de Clima para Telegram

Este es un bot de Telegram que consulta el clima actual de cualquier ciudad usando la API de OpenWeather.

## Funcionalidades

- Comando `/clima <ciudad>`: Devuelve la temperatura, humedad, viento y descripción del clima con emojis.
- Comando `/start`: Mensaje de bienvenida.
- Comando `/help`: Muestra la ayuda con los comandos disponibles.

## Requisitos

- Python 3.8 o superior
- Librerías:
  - python-telegram-bot==20.3
  - requests

## Instalación

1. Clona el repositorio o descarga el código.
2. Instala las dependencias con:

   ```bash
   pip install python-telegram-bot==20.3 requests
   ```

3. Crea un bot en Telegram y consigue tu token [aquí](https://core.telegram.org/bots#6-botfather).
4. Consigue una API key de OpenWeather en [https://openweathermap.org/api](https://openweathermap.org/api).

5. Configura las variables `TOKEN` y `WEATHER_API_KEY` en el archivo principal.

## Uso

Ejecuta el bot con:

```bash
python bot_clima.py
```

Luego en Telegram escribe:

```
/start
/clima Vigo
/help
```

## Licencia

Este proyecto es libre para uso personal y educativo.

---

Si quieres te ayudo también con comandos Git para subirlo a GitHub. ¿Quieres?
