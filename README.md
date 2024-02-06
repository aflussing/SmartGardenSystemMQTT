# Smart Garden System MQTT

El Smart Garden System es un sistema integrado de monitorización y control para jardinería inteligente que utiliza MQTT y Tkinter. Este proyecto innovador incluye clientes MQTT para sensores de temperatura, humedad y color de las hojas, junto con un motor de agua que automatiza el riego, proporcionando una solución completa para el cuidado de plantas. Es ideal para entusiastas de la jardinería, proyectos de agricultura urbana y educación en IoT, ofreciendo una manera eficiente y tecnológica de mantener un jardín saludable.

## Requisitos Previos

Antes de comenzar, necesitarás Docker y Docker Compose instalados en tu sistema. Para obtener instrucciones detalladas de instalación, visita:

- [Instalar Docker](https://docs.docker.com/get-docker/)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Cómo Usar

### Configurar el Entorno con Docker Compose

Para iniciar todos los servicios necesarios, incluyendo el servidor MQTT y los clientes MQTT, navega al directorio del proyecto en una terminal y ejecuta:

```bash
docker-compose up -d
```

Este comando levantará los contenedores definidos en tu `docker-compose.yml`, estableciendo la base para tu sistema de jardinería inteligente.

### Ejecutar el Script de Python

Con el entorno corriendo, inicia el script `start_clients.py` para activar los clientes MQTT y el panel de control Tkinter. Asegúrate de que Python y todas las dependencias necesarias estén instaladas en tu sistema, luego ejecuta:

```bash
python start_clients.py
```

### Finalizar el Entorno

Cuando necesites detener y eliminar todos los contenedores, utiliza:

```bash
docker-compose down
```

## Contribuciones

Si estás interesado en mejorar el Smart Garden System, tus contribuciones son bienvenidas. Por favor, lee las directrices de contribución para empezar.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT, lo que permite a los usuarios usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del software bajo los términos establecidos. Para más detalles, consulta el archivo `LICENSE`.
