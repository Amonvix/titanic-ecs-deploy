# syntax=docker/dockerfile:1
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala pacotes Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

# Dá permissão de execução ao entrypoint
RUN chmod +x ./entrypoint.sh

# Comando de inicialização
ENTRYPOINT ["./entrypoint.sh"]
