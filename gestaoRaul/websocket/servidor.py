import asyncio
import websockets
import json
import logging
import uuid


# Configurar o registro de logs
logging.basicConfig(level=logging.INFO)

connected_clients = set()

async def handle_client(websocket):
    logging.info(f"Cliente conectado: {websocket.remote_address}")
    connected_clients.add(websocket)
    # for client in connected_clients:
    #     await client.send(json.dumps({"message": "Novo cliente conectado"}))
        # print(client)
    try:
        async for message in websocket:
            logging.info(f"Mensagem recebida de {websocket.remote_address}: {message}")
            print(f"Mensagem recebida de {websocket.remote_address}: {message}")
            try:
                data = json.loads(message)
                # Processa a mensagem aqui
                await process_message(data, websocket)

            except json.JSONDecodeError:
                logging.error(f"JSON inválido recebido de {websocket.remote_address}: {message}")
                await websocket.send(json.dumps({"error": "Formato JSON inválido"}))
            except Exception as e:
                logging.error(f"Erro ao processar mensagem de {websocket.remote_address}: {e}")
                await websocket.send(json.dumps({"error": "Erro ao processar mensagem"}))

    except websockets.exceptions.ConnectionClosedOK:
        logging.info(f"Cliente desconectado: {websocket.remote_address}")
    except websockets.exceptions.ConnectionClosedError:
        logging.error(f"Conexão do cliente fechada com erro {websocket.remote_address}")
    except Exception as e:
      logging.error(f"Erro durante a conexão de {websocket.remote_address} com erro {e}")
    finally:
        connected_clients.remove(websocket)

async def process_message(data, websocket):
    if "type" in data and data["type"] == "broadcast" and "message" in data:
        await broadcast_message(data)
        print("Mensagem de Broadcast:", data["message"])
    elif "type" in data and data["type"] == "echo" and "message" in data:
        await websocket.send(json.dumps({"response": data['message']}))
    elif "type" in data and data['type'] == "test":
        await websocket.send(json.dumps({"response": "teste está ok"}))
    else:
        logging.warning(f"Tipo de mensagem ou formato desconhecido: {data}")
        await websocket.send(json.dumps({"error": "Tipo de mensagem desconhecido"}))
      
async def broadcast_message(data):
    if connected_clients:
        logging.info(f"Enviando mensagem por broadcast: {data}")
        # await asyncio.wait([client.send(json.dumps(data)) for client in connected_clients])
        tasks = [asyncio.create_task(client.send(json.dumps(data))) for client in connected_clients]
        await asyncio.wait(tasks)
    else:
        logging.info("Nenhum cliente conectado.")


async def main():
    start_server = websockets.serve(handle_client, "192.168.1.150", 8765)
    logging.info("Servidor WebSocket iniciado em ws://192.168.1.150:8765")
    await start_server
    await asyncio.Future()  # Mantém o servidor em execução indefinidamente


if __name__ == "__main__":
    asyncio.run(main())
