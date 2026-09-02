FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev

# Se especifican las versiones mínimas seguras requeridas por Trivy
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]