import asyncio
import websockets
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

connected_clients = set()  # Keep track of connected clients

async def handle_client(websocket): # Remove 'path' argument
    """Handles a single client connection."""
    logging.info(f"Client connected: {websocket.remote_address}")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            logging.info(f"Received message from {websocket.remote_address}: {message}")
            print(f"Received message from {websocket.remote_address}: {message}")
            try:
                data = json.loads(message)
                # Process the message here
                await process_message(data, websocket)

            except json.JSONDecodeError:
                logging.error(f"Invalid JSON received from {websocket.remote_address}: {message}")
                await websocket.send(json.dumps({"error": "Invalid JSON format"}))
            except Exception as e:
                logging.error(f"Error processing message from {websocket.remote_address}: {e}")
                await websocket.send(json.dumps({"error": "Error processing message"}))

    except websockets.exceptions.ConnectionClosedOK:
        logging.info(f"Client disconnected: {websocket.remote_address}")
    except websockets.exceptions.ConnectionClosedError:
        logging.error(f"Client connection closed with error {websocket.remote_address}")
    except Exception as e:
      logging.error(f"Error during connection from {websocket.remote_address} with error {e}")
    finally:
        connected_clients.remove(websocket)

async def process_message(data, websocket):
    """Processes the received message and takes actions."""
    # Example: check if it's a broadcast message
    if "type" in data and data["type"] == "broadcast" and "message" in data:
        await broadcast_message(data)
        print("Broadcast message:", data["message"])
    elif "type" in data and data["type"] == "echo" and "message" in data:
        await websocket.send(json.dumps({"response": data['message']}))
    elif "type" in data and data['type'] == "test":
        await websocket.send(json.dumps({"response": "test is ok"}))
    else:
        logging.warning(f"Unknown message type or format: {data}")
        await websocket.send(json.dumps({"error": "Unknown message type"}))
      
async def broadcast_message(data):
    """Broadcasts a message to all connected clients."""
    if connected_clients:
        logging.info(f"Broadcasting message: {data}")
        await asyncio.wait([client.send(json.dumps(data)) for client in connected_clients])
    else:
        logging.info("No clients connected. Message not broadcasted.")


async def main():
    """Starts the WebSocket server."""
    start_server = websockets.serve(handle_client, "localhost", 8765)
    logging.info("WebSocket server started on ws://localhost:8765")
    await start_server
    await asyncio.Future()  # Keep the server running indefinitely


if __name__ == "__main__":
    asyncio.run(main())
