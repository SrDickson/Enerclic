FROM python:3.8-slim

WORKDIR /app

COPY server.py .

RUN pip install asyncio

CMD ["python", "server.py"]
