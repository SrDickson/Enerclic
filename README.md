# Prueba Técnica Python

La prueba consistiría en realizar un chat entre dos PC usando Python en una arquitectura clientes/servidor.

Script a) - Servidor

Script b) - Clientes

El objetivo es que 2 clientes se conecten al servidor, y a partir de ahí, 
ambos puedan intercambiarse mensajes.

Todos los mensajes, los debes guardar en un log de mensajes.
Los mensajes a enviar deben ser de forma asíncrona (enviar mensajes sin necesidad de una recepción previa).
El sistema debe ser dockerizado, al menos en un docker. 
Se valorará la creación de docker cliente y docker servidor.

- Enerclic:
  - client.py
  - server.py
  - Dockerfile
  # Dependiendo de tu SO
  - script linux-macOS.sh 
  # Dependiendo de tu SO
  - script windows.bat 
  - README.md
  
1.- Instalaremos docker desktop:
    https://docs.docker.com/get-docker/

2.-Una vez instalado docker, instalaremos Python.
    https://www.python.org/downloads/

3.- Una vez todo instalado, iremos al directorio y ejecutaremos el script
    script windows.bat  / script linux-macOS.sh

4.- El script montará el contenedor del servidor y abrirá 2 clientes para comenzar el chat.


# Enlaces y Recursos

- Documentación:
  - Docker - https://docs.docker.com/
  - Python - https://docs.python.org/3/
