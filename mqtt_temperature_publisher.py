import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
port = 1883
topic = "temperature-sensor"

client = mqtt.Client("TemperaturePublisher")
client.connect(broker_address, port=port)

# Simula una temperatura inicial y variaciones
temperature = 20  # Temperatura inicial en grados Celsius

while True:
    # Simula una variación de temperatura
    variation = random.uniform(-0.5, 0.5)  # Variación máxima de +/-0.5 grados
    temperature += variation

    # Asegura que la temperatura esté dentro de un rango razonable
    temperature = max(15, min(temperature, 25))  # Mantiene la temperatura entre 15 y 25 grados

    message = f"Temperatura {temperature:.2f} grados"
    client.publish(topic, message)
    print(f"Mensaje enviado: {message}")

    time.sleep(5)  # Espera 5 segundos antes de enviar el siguiente mensaje

