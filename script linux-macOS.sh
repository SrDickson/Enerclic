#!/bin/bash

docker build -t chat_server -f Dockerfile .

docker run -d --name chat_server -p 8888:8888 chat_server

sleep 2

gnome-terminal -- python client.py
gnome-terminal -- python client.py
