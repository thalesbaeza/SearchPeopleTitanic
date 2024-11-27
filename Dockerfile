# Use uma imagem oficial do Python como base
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY . /app

# Instala as dependências necessárias
RUN pip install --no-cache-dir psycopg2-binary

# Define o comando padrão ao rodar o contêiner
CMD ["python"]