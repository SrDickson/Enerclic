# Python Technical Test

The test would consist of making a chat between two PCs using Python in a clients/server architecture.

Script a) - Server

Script b) - Clients

The goal is for 2 clients to connect to the server, and from there,
Both can exchange messages.

You must save all messages in a message log.
The messages to be sent must be asynchronous (send messages without prior reception).
The system must be dockerized, at least in one docker.
The creation of docker client and docker server will be considered.

- Enerclic:
   - client.py
   - server.py
   - Dockerfile
   # Depending on your OS
   - linux-macOS.sh script
   # Depending on your OS
   - windows.bat script
  
1.- We will install docker desktop:
     https://docs.docker.com/get-docker/

2.-Once docker is installed, we will install Python.
     https://www.python.org/downloads/

3.- Once everything is installed, we will go to the directory and execute the script
     script windows.bat / script linux-macOS.sh

4.- The script will mount the server container and open 2 clients to start the chat.


# Links and Resources

- Documentation:
   - Docker - https://docs.docker.com/
   - Python - https://docs.python.org/3/
