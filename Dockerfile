# Use uma imagem Python slim
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para rodar a aplicação com gunicorn via WSGI
CMD ["gunicorn", "titanic_project.wsgi:application", "--bind", "0.0.0.0:8000"]
