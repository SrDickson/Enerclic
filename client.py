import asyncio
import logging


class Client:
    def __init__(self, host, port):
        # Initialize the Client object with the specified host and port
        self.host = host
        self.port = port

        # Create a logging object for the client
        self.log = logging.getLogger('client')

    async def send_message(self, writer, message):
        try:
            # Encode the message and write it to the writer
            writer.write(message.encode())

            # Ensure that the data is flushed before continuing
            await writer.drain()
        except asyncio.CancelledError:
            # Handle cancellation gracefully by ignoring it
            pass

    async def receive_messages(self, reader):
        try:
            while True:
                # Continuously read messages (up to 100 bytes) from the reader
                message = await reader.read(100)

                # Break the loop if an empty message is received
                if not message:
                    break

                # Print the received message after decoding it
                print(f"Received message: {message.decode()}")
        except asyncio.CancelledError:
            # Handle cancellation gracefully by ignoring it
            pass

    async def start_client(self):
        try:
            # Establish a connection with the specified host and port
            reader, writer = await asyncio.open_connection(self.host, self.port)

            # Start a task to receive messages in the background
            receive_task = asyncio.create_task(self.receive_messages(reader))

            while True:
                # Continuously prompt the user for input
                user_input = input("Enter your message: ")

                # Send the user input as a message
                await self.send_message(writer, user_input)

                # Sleep for a short duration to avoid excessive CPU usage
                await asyncio.sleep(0.1)

        except asyncio.CancelledError:
            # Handle cancellation gracefully by ignoring it
            pass

        finally:
            # Cancel the task to receive messages before closing the connection
            receive_task.cancel()

            # Close the writer and wait for the connection to be fully closed
            writer.close()
            await writer.wait_closed()


if __name__ == "__main__":
    # Set up basic logging with the INFO level
    logging.basicConfig(level=logging.INFO)

    # Create a Client instance with a specified host ('127.0.0.1') and port (8888)
    client = Client('127.0.0.1', 8888)

    # Run the asynchronous start_client method using asyncio.run()
    asyncio.run(client.start_client())
