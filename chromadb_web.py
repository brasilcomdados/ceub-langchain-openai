import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

import uuid  # Biblioteca para geração de IDs únicos

# Carregar variáveis de ambiente
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', default='')
OPENAI_ID_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")

# Inicializa os embeddings OpenAI
embeddings_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY, openai_organization=OPENAI_ID_ORGANIZATION)

# Carrega o documento
loader = WebBaseLoader([
    "https://consultaremedios.com.br/anador/bula",
    "https://consultaremedios.com.br/creme-preventivo-contra-assadura-hipoglos-transparente/30g-1/p#description",
    "https://consultaremedios.com.br/sorine-nebulizador/0-9-frasco-gotejador-com-45ml-de-solucao-de-uso-nasal-bico-nebulizador/p#leaflet_description",
    "https://consultaremedios.com.br/lisador/500mg-5mg-10mg-caixa-com-24-comprimidos/p#leaflet_description",
    "https://consultaremedios.com.br/doril-enxaqueca/250mg-250mg-65mg-caixa-com-18-comprimidos-revestidos/p#leaflet_description",
    "https://consultaremedios.com.br/doril-enxaqueca/p#leaflet_description"

])

data = loader.load()

# Dividir documentos em chunks de texto
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = text_splitter.split_documents(data)

# Cria um banco vetorizado ChromaDB e persiste os chunks de texto
vstore = Chroma.from_documents(chunks, embeddings_model, persist_directory='db')

# Imprime o número de chunks e a informação do banco vetorizado
print(len(chunks), vstore)