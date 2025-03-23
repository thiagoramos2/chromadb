# Usar uma imagem base do Python
FROM python:3.9-slim

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install chromadb faiss-cpu

# Definir diretório de trabalho
WORKDIR /app

# Copiar o código do repositório para o container
COPY . /app

# Comando para rodar o servidor
CMD ["python", "main.py"]

