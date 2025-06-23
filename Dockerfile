# Usa uma imagem Python slim
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 1. Dê permissão de execução para o seu script
RUN chmod +x /app/entrypoint.sh

# Expõe a porta que a aplicação vai usar
EXPOSE 8001

# 2. Defina o seu script como o "ponto de entrada" do contêiner.
# A linha CMD antiga foi removida, pois o comando já está no entrypoint.
ENTRYPOINT [ "/app/entrypoint.sh" ]