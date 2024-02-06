import tkinter as tk
from tkinter import scrolledtext
import paho.mqtt.client as mqtt

# Configura aquí tu servidor MQTT
mqtt_broker = 'localhost'
mqtt_port = 1883
mqtt_topic = '#'  # Suscribirse a todos los topics para demostración

# Cliente MQTT
class MqttClient:
    def __init__(self, gui):
        self.gui = gui
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect(mqtt_broker, mqtt_port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(mqtt_topic)

    def on_message(self, client, userdata, msg):
        message = f"Topic: {msg.topic}\nMessage: {str(msg.payload.decode('utf-8'))}\n"
        self.gui.display_message(message)

# Interfaz de usuario Tkinter
class MqttGui:
    def __init__(self, master):
        self.master = master
        master.title("MQTT Topics and Messages")
        
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state='disabled')

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.yview(tk.END)
        self.text_area.config(state='disabled')

def main():
    root = tk.Tk()
    gui = MqttGui(root)
    mqtt_client = MqttClient(gui)
    mqtt_client.connect()
    root.mainloop()

if __name__ == "__main__":
    main()

