import paho.mqtt.client as mqtt
import random
import time
import json

# Setări pentru conexiunea MQTT
broker = "mqtt.beia-telemetrie.ro"  
port = 1883
topic = "/training/device/Eduard-Radu/"

# Funcție pentru a genera valori random pentru temperatură, presiune, umiditate și gaz
def generate_sensor_data():
    temperature = round(random.uniform(15.0, 30.0), 2)
    pressure = round(random.uniform(900.0, 1050.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    gas = round(random.uniform(0.0, 100.0), 2)
    return {
        "temperature": temperature,
        "pressure": pressure,
        "humidity": humidity,
        "gas": gas
    }

# Conectare la broker-ul MQTT
client = mqtt.Client()
client.connect(broker, port, 60)

# Loop pentru a trimite date la un interval de 5 secunde
try:
    while True:
        sensor_data = generate_sensor_data()
        client.publish(topic, json.dumps(sensor_data))
        print(f"Sent: {sensor_data}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Interrupted")
    client.disconnect()
