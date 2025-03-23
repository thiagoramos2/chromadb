import chromadb
from chromadb.config import Settings

# Inicializar o cliente do ChromaDB
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./db"))

# Criar uma coleção para armazenar os materiais
collection = client.create_collection("materiais_consorcio")

# Adicionar um documento de exemplo
document = "O consórcio é uma modalidade de compra baseada em grupo."
embedding = [0.12, 0.23, 0.45]  # Este é um vetor de exemplo, substitua pelo vetor de embeddings real

collection.add(
    documents=[document],
    embeddings=[embedding],
    metadatas=[{"source": "material1"}],
    ids=["doc1"]
)

# Consulta um documento usando um vetor de embedding de consulta
query = "O que é consórcio?"
query_embedding = [0.15, 0.25, 0.48]  # Substitua pelo vetor de embedding real da consulta

# Realiza a consulta e retorna o documento mais relevante
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

# Exibe o resultado
print("Resultados da consulta:", results['documents'])

