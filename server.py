
# For asynchronous programming and logging
import asyncio
import logging


class Server:
    def __init__(self, host, port):
        # Initialize the Server object with the specified host and port
        self.host = host
        self.port = port

        # Set to keep track of connected clients
        self.clients = set()

        # Create a logging object for the server
        self.log = logging.getLogger('server')

    async def handle_client(self, reader, writer):
        # Add the writer to the set of connected clients
        self.clients.add(writer)

        # Get the address information of the connected client
        address = writer.get_extra_info('peername')
        self.log.info(f"New connection from {address}")

        try:
            while True:
                # Continuously read data (up to 100 bytes) from the client
                data = await reader.read(100)
                if not data:
                    break

                # Decode the received data into a message
                message = data.decode()
                self.log.info(f"Received message from {address}: {message}")

                # Broadcast the message to all connected clients except the sender
                await self.broadcast(message, writer)

        except asyncio.CancelledError:
            # Handle cancellation gracefully by ignoring it
            pass

        finally:
            # Log the closure of the connection
            self.log.info(f"Connection closed from {address}")

            # Remove the writer from the set of connected clients
            self.clients.remove(writer)

            # Close the writer and wait for the connection to be fully closed
            writer.close()
            await writer.wait_closed()

    async def broadcast(self, message, sender):
        # Log the broadcasted message
        self.log.info(f"Broadcasting message: {message}")

        # Iterate through all connected clients
        for client in self.clients:
            if client != sender:
                try:
                    # Encode and write the message to each client
                    client.write(message.encode())

                except (asyncio.CancelledError, BrokenPipeError, OSError):
                    # Ignore exceptions related to writing to the socket
                    pass

    async def start_server(self):
        # Start the server and handle incoming connections using the handle_client method
        server = await asyncio.start_server(self.handle_client, self.host, self.port)

        # Use 'async with' to ensure proper cleanup when the server is stopped
        async with server:
            # Serve incoming connections indefinitely
            await server.serve_forever()


if __name__ == "__main__":
    # Set up basic logging with the INFO level
    logging.basicConfig(level=logging.INFO)

    # Create a Server instance with a specified host ('0.0.0.0') and port (8888)
    server = Server('0.0.0.0', 8888)

    # Run the asynchronous start_server method using asyncio.run()
    asyncio.run(server.start_server())
