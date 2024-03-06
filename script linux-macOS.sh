#!/bin/bash

# Construir la imagen del servidor
docker build -t chat_server -f Dockerfile .

# Ejecutar el contenedor del servidor en segundo plano
docker run -d --name chat_server -p 8888:8888 chat_server

# Esperar un breve momento antes de iniciar los clientes
sleep 2

# Ejecutar clientes en dos terminales de sistema diferentes
gnome-terminal -- python client.py
gnome-terminal -- python client.py
