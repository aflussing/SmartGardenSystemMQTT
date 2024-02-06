import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
port = 1883
topic = "leaf-color-sensor"

client = mqtt.Client("LeafColorSensor")
client.connect(broker_address, port=port)

while True:
    color_index = random.randint(1, 5)  # Simula una lectura del color de las hojas
    message = f"Índice de color de las hojas: {color_index}"
    client.publish(topic, message)
    print(f"Mensaje enviado: {message}")
    time.sleep(5)

