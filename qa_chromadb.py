import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA

# Carregar variáveis de ambiente
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', default='')
OPENAI_ID_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")

# Inicializa os embeddings OpenAI
embeddings_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY, openai_organization=OPENAI_ID_ORGANIZATION)

# # load from disk
db = Chroma(persist_directory="db", embedding_function=embeddings_model)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})

model = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever,
                                    return_source_documents=False)

# question = "qual o medicamento eu posso usar para dores de cabeça? Cite nomes comerciais"
question = "Estou com dores de cabeça, quais medicamentos são indicados?"
response = model.invoke(question)
print(response)
