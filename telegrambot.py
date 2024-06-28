from quart import Quart, request
import requests
import asyncio
from telegram import Bot, Update

app = Quart(__name__)
bot_token = 'your_API'

# Initialize bot
bot = Bot(token=bot_token)

# InfluxDB settings
INFLUXDB_URL = "http://yout_id:8086"
INFLUXDB_DB = "sensor_data"  # Name of your InfluxDB database

async def send_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

async def start(update):
    await send_message(update.message.chat_id, 'Hi! Use /temperature, /pressure, /humidity, or /gas to get the latest readings.')

async def get_temperature(update):
    try:
        response = requests.get(f"{INFLUXDB_URL}/query", params={
            "q": f"SELECT last(temperature) FROM {INFLUXDB_DB}",
            "db": INFLUXDB_DB
        })
        data = response.json()
        print("Temperature response:", data)
        if 'results' in data and data['results'][0].get('series'):
            temperature = data['results'][0]['series'][0]['values'][0][1]
            print(f"Temperature value: {temperature}")
            await send_message(update.message.chat_id, f"Current temperature: {temperature}°C")
        else:
            print("No temperature data found.")
            await send_message(update.message.chat_id, "No temperature data found.")
    except Exception as e:
        print("Error fetching temperature:", e)
        await send_message(update.message.chat_id, "Error fetching temperature data.")

async def get_pressure(update):
    try:
        response = requests.get(f"{INFLUXDB_URL}/query", params={
            "q": f"SELECT last(pressure) FROM {INFLUXDB_DB}",
            "db": INFLUXDB_DB
        })
        data = response.json()
        print("Pressure response:", data)
        if 'results' in data and data['results'][0].get('series'):
            pressure = data['results'][0]['series'][0]['values'][0][1]
            print(f"Pressure value: {pressure}")
            await send_message(update.message.chat_id, f"Current pressure: {pressure} hPa")
        else:
            print("No pressure data found.")
            await send_message(update.message.chat_id, "No pressure data found.")
    except Exception as e:
        print("Error fetching pressure:", e)
        await send_message(update.message.chat_id, "Error fetching pressure data.")

async def get_humidity(update):
    try:
        response = requests.get(f"{INFLUXDB_URL}/query", params={
            "q": f"SELECT last(humidity) FROM {INFLUXDB_DB}",
            "db": INFLUXDB_DB
        })
        data = response.json()
        print("Humidity response:", data)
        if 'results' in data and data['results'][0].get('series'):
            humidity = data['results'][0]['series'][0]['values'][0][1]
            print(f"Humidity value: {humidity}")
            await send_message(update.message.chat_id, f"Current humidity: {humidity}%")
        else:
            print("No humidity data found.")
            await send_message(update.message.chat_id, "No humidity data found.")
    except Exception as e:
        print("Error fetching humidity:", e)
        await send_message(update.message.chat_id, "Error fetching humidity data.")

async def get_gas(update):
    try:
        response = requests.get(f"{INFLUXDB_URL}/query", params={
            "q": f"SELECT last(gas) FROM {INFLUXDB_DB}",
            "db": INFLUXDB_DB
        })
        data = response.json()
        print("Gas response:", data)
        if 'results' in data and data['results'][0].get('series'):
            gas = data['results'][0]['series'][0]['values'][0][1]
            print(f"Gas value: {gas}")
            await send_message(update.message.chat_id, f"Current gas level: {gas} PPM")
        else:
            print("No gas data found.")
            await send_message(update.message.chat_id, "No gas data found.")
    except Exception as e:
        print("Error fetching gas:", e)
        await send_message(update.message.chat_id, "Error fetching gas data.")

@app.route('/webhook', methods=['POST'])
async def webhook():
    update = Update.de_json(await request.get_json(), bot)
    await handle_update(update)
    return 'ok'

async def handle_update(update):
    if update.message:
        print(f"Handling message: {update.message.text}")
        if update.message.text == '/start':
            await start(update)
        elif update.message.text == '/temperature':
            await get_temperature(update)
        elif update.message.text == '/pressure':
            await get_pressure(update)
        elif update.message.text == '/humidity':
            await get_humidity(update)
        elif update.message.text == '/gas':
            await get_gas(update)
        else:
            await send_message(update.message.chat_id, "Unknown command")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)
