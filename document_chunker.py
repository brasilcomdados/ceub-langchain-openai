from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Carrega o documento a partir da URL fornecida
loader = WebBaseLoader("https://consultaremedios.com.br/anador/bula")


def verbose_data(data):
    # Extrai o primeiro documento (neste caso há um único documento)
    document = data[0]

    # Chaves do dicionário
    print(document.__dict__.keys())

    # Visualiza os 100 primeiros caracteres
    print(document.page_content[:2])

    # Visualizar todos
    print(document.page_content)

    # Metadados
    print(document.metadata)


# Carrega os dados do documento a partir da URL
data = loader.load()

# Dividir documentos em chunks de texto
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = text_splitter.split_documents(data)

# Exibe o primeiro chunk de texto
print(chunks[0])
