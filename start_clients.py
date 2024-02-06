import subprocess
import time

# Lista de comandos para iniciar cada cliente
clients = [
    # "python mqtt_kivy_panel.py",
    "python mqtt_tkinter_panel.py",
    "python mqtt_temperature_publisher.py",
    "python mqtt_humidity_sensor.py",
    "python mqtt_leaf_color_sensor.py",
    "python mqtt_water_motor.py"
]

processes = []

try:
    # Iniciar todos los clientes
    for client in clients:
        print(f"Iniciando: {client}")
        proc = subprocess.Popen(client, shell=True)
        processes.append(proc)

    # Esperar a que el panel de control Tkinter (primer proceso) termine
    processes[0].wait()

finally:
    # Una vez que el panel Tkinter se cierra, terminar los demás procesos
    for proc in processes[1:]:
        proc.terminate()
    print("Todos los clientes han sido terminados.")

