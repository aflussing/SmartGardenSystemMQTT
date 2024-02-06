import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import paho.mqtt.client as mqtt

# Configura aquí tu servidor MQTT
mqtt_broker = 'localhost'
mqtt_port = 1883
mqtt_topic = '#'  # Suscribirse a todos los topics para demostración

# Cliente MQTT
class MqttClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.messages = []

    def connect(self):
        self.client.connect(mqtt_broker, mqtt_port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(mqtt_topic)

    def on_message(self, client, userdata, msg):
        message = f"Topic: {msg.topic}\nMessage: {str(msg.payload.decode('utf-8'))}"
        print(message)
        self.messages.append(message)

mqtt_client = MqttClient()

# Interfaz de usuario Kivy
class MqttPanel(BoxLayout):
    def update_messages(self, dt):
        self.clear_widgets()
        for message in mqtt_client.messages[-10:]:  # Muestra los últimos 10 mensajes
            self.add_widget(Label(text=message, size_hint_y=None, height=40))

class MqttApp(App):
    def build(self):
        mqtt_client.connect()
        panel = MqttPanel(orientation='vertical')
        Clock.schedule_interval(panel.update_messages, 1)  # Actualiza los mensajes cada segundo
        return panel

if __name__ == '__main__':
    MqttApp().run()
r
