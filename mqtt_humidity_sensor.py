import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
port = 1883
topic = "humidity-sensor"

client = mqtt.Client("HumiditySensor")
client.connect(broker_address, port=port)

while True:
    humidity = random.randint(30, 70)  # Simula una lectura de humedad
    message = f"Humedad de la tierra: {humidity}%"
    client.publish(topic, message)
    print(f"Mensaje enviado: {message}")
    time.sleep(5)

