# Usa uma imagem Python slim
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# 1. Copie APENAS o arquivo de dependências primeiro.
COPY requirements.txt .

# 2. Instale as dependências. Esta camada só será refeita se o requirements.txt mudar.
RUN pip install --no-cache-dir -r requirements.txt

# 3. AGORA SIM, copie o resto do código da sua aplicação.
COPY . .

# Dê permissão de execução para o seu script
RUN chmod +x /app/entrypoint.sh

# Expõe a porta que a aplicação vai usar
EXPOSE 8001

# Define o seu script como o "ponto de entrada" do contêiner.
ENTRYPOINT [ "/app/entrypoint.sh" ]