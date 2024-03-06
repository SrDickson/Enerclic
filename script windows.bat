@echo off

docker build -t chat_server -f Dockerfile .

docker run -d --name chat_server -p 8888:8888 chat_server

timeout /t 2

start cmd /k python.exe client.py
start cmd /k python.exe client.py
