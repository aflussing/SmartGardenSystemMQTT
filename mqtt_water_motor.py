import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 1883
subscribe_topic = "humidity-sensor"
publish_topic = "water-motor"

def on_message(client, userdata, message):
    humidity = int(message.payload.decode("utf-8").split(": ")[1].rstrip("%"))
    if humidity < 40:  # Umbral de humedad para activar el motor
        client.publish(publish_topic, "Motor de agua encendido debido a baja humedad")
        print("Motor de agua encendido")
    else:
        print("Humedad suficiente, el motor de agua permanece apagado")

client = mqtt.Client("WaterMotor")
client.connect(broker_address, port=port)
client.subscribe(subscribe_topic)
client.on_message = on_message

client.loop_forever()

