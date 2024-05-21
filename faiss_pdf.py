import os
import faiss
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', default='')
OPENAI_ID_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")


def load_or_create_faiss_index(file_path, pages, embeddings_model):
    """ Carrega um índice FAISS existente do disco ou cria um novo se não existir. """
    if os.path.exists(file_path):
        print("Carregando índice FAISS existente.")
        index = faiss.read_index(file_path)
        return FAISS.from_precomputed_index(index)
    else:
        print("Criando novo índice FAISS.")
        faiss_index = FAISS.from_documents(pages, embeddings_model)
        # Precisamos acessar o índice interno de maneira correta. Supondo que faiss_index agora tem uma propriedade para acessar.
        faiss.write_index(faiss_index.index, file_path)  # Garante que o índice é salvo para uso futuro
        return faiss_index


def main():
    # Carrega o documento PDF e divide em páginas
    loader = PyPDFLoader("pdf/bi000043.pdf")
    pages = loader.load_and_split()

    # Inicializa os embeddings OpenAI
    embeddings_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY, openai_organization=OPENAI_ID_ORGANIZATION)

    # Carrega ou cria o índice FAISS
    index_file = "db_index.faiss"
    faiss_index = load_or_create_faiss_index(index_file, pages, embeddings_model)

    # Realiza uma busca por similaridade no índice FAISS
    search_query = "O que Veloso pediu para Montenegro preparar enquanto ele saía para comprar estampilhas?"
    docs = faiss_index.similarity_search(search_query, k=3)

    # Imprime os resultados da busca
    for doc in docs:
        print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}')


if __name__ == "__main__":
    main()

"""
De onde são originários Montenegro e Veloso?
Por que Montenegro e Veloso acham que talvez nunca mais se encontrem?
Qual é a opinião compartilhada por Montenegro e Veloso sobre o casamento?
Qual aposta Montenegro e Veloso fazem e qual é o valor dela?
O que Veloso pediu para Montenegro preparar enquanto ele saía para comprar estampilhas?
"""

# http://www.dominiopublico.gov.br/download/texto/bi000043.pdf