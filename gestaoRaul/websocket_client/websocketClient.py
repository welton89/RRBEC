import websockets
import asyncio
import json

async def enviar_mensagem(msg):
    uri = "ws://websocket_server:8765"

    try:
        async with websockets.connect(uri) as websocket:
            # Garante que msg seja JSON
            if isinstance(msg, dict):
                mensagem_json = json.dumps(msg)
            else:
                mensagem_json = str(msg)

            await websocket.send(mensagem_json)
            print(f"> Enviado: {mensagem_json}")

            # Se quiser esperar uma resposta (opcional)
            # resposta = await websocket.recv()
            # print(f"< Recebido: {resposta}")

    except websockets.exceptions.InvalidURI as e:
        print(f"URI inválida: {e}")
    except websockets.exceptions.InvalidHandshake as e:
        print(f"Handshake WebSocket falhou: {e}")
    except ConnectionRefusedError:
        print("Conexão recusada. Verifique se o servidor WebSocket está rodando.")
    except Exception as e:
        print(f"Erro ao enviar mensagem via websocket: {e}")
