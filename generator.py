import os
import logging
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import pprint

# Configurar o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Carregar as variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', default='')
OPENAI_ID_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")


def create_llm_client(api_key, organization):
    """Cria um cliente para o modelo de linguagem."""
    if not api_key or not organization:
        logging.error("API key or organization is not set.")
        raise ValueError("API key and organization must be set in the environment.")
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=api_key,
        openai_organization=organization,
    )


def generate_name(segment="Pets"):
    """Gera nomes de empresas para um segmento de mercado específico."""
    try:
        # Inicializa o cliente do modelo de linguagem usando as credenciais fornecidas.
        llm = create_llm_client(OPENAI_API_KEY, OPENAI_ID_ORGANIZATION)

        # Envia as mensagens para o modelo de linguagem. A primeira mensagem define o contexto de que
        # o assistente deve sempre responder em Português do Brasil. A segunda mensagem solicita ao modelo
        # para gerar cinco ideias de nomes de empresas baseadas no segmento de mercado especificado.
        response = llm.invoke([
            SystemMessage(content="Você é um assistente IA que sempre responde em Português do Brasil"),
            HumanMessage(content=f"Gere 5 ideias de nomes para empresas no segmento {segment}")
        ])

        # Retorna a resposta do modelo, que idealmente contém os nomes de empresas sugeridos.
        return response
    except Exception as e:
        logging.error(f"Failed to generate company name: {e}")
        return None


def format_response(response):
    # Extrair informações relevantes
    content = response.content
    metadata = response.response_metadata
    token_usage = metadata.get('token_usage')
    model_name = metadata.get('model_name')
    finish_reason = metadata.get('finish_reason')

    # Formatar a saída
    print("Resposta da IA:")
    print(content)  # Usando print diretamente para respeitar \n
    print("\nMetadados da Resposta:")
    print(f"Modelo Utilizado: {model_name}")
    print(f"Razão de Conclusão: {finish_reason}")
    print("Uso de Tokens:")
    print(f"Tokens de Conclusão: {token_usage['completion_tokens']}")
    print(f"Tokens de Prompt: {token_usage['prompt_tokens']}")
    print(f"Total de Tokens: {token_usage['total_tokens']}")


if __name__ == "__main__":
    segment = "Salão de Beleza"
    company_names = generate_name(segment)
    if company_names:
        format_response(company_names)
    else:
        print("Não foi possível gerar nomes de empresas.")
