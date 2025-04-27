
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get clean

RUN git clone https://github.com/welton89/websocket-RRBEC.git /app

RUN pip install --upgrade pip && pip install websockets

EXPOSE 8765

CMD ["python", "websocket_server.py"]
