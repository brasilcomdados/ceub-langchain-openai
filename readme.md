# Projeto de Integração LangChain e OpenAI

Este projeto foi desenvolvido para demonstrar a integração da biblioteca LangChain com a API da OpenAI. Ele foi
apresentado para uma turma do CEUB e exemplifica como utilizar o modelo de linguagem da OpenAI para gerar respostas a
perguntas específicas.

## Pré-requisitos

Antes de executar o código, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas `langchain_openai`, `python-dotenv`, `chromadb`, e `faiss-cpu`

Para instalar as dependências, você pode usar o seguinte comando:

```bash
pip install langchain-openai python-dotenv chromadb faiss-cpu
```

## Configuração do Ambiente Virtual

Recomendamos o uso de um ambiente virtual para gerenciar as dependências do projeto. Para instalar e configurar um
ambiente virtual usando virtualenv no Linux, siga as instruções na documentação oficial: Guia de Instalação do
Virtualenv.

Após instalar o virtualenv, crie e ative seu ambiente virtual:

```bash
# Instale o virtualenv
pip install virtualenv

# Crie um ambiente virtual
virtualenv venv

# Ative o ambiente virtual
source venv/bin/activate
```

## Configuração

Crie um arquivo .env na raiz do projeto e adicione suas chaves de API da OpenAI, como mostrado abaixo:

```
OPENAI_API_KEY=your_openai_api_key
OPENAI_ORGANIZATION=your_openai_organization_id
```

## Estrutura do Projeto

- `simple.py`: Script principal contendo a lógica de integração com a OpenAI.
- `generator.py`: Script para geração de nomes de empresas utilizando a OpenAI.
- `document_chunker.py`: Script para extrair dados de uma URL e dividir o texto do documento em chunks menores.
- `faiss_pdf.py`: Script que demonstra como extrair informações de um arquivo PDF, persistir esses dados em um índice
  FAISS e realizar buscas por similaridade para interagir com o conteúdo do PDF. Este projeto enfatiza o uso de um banco
  vetorizado para armazenar e buscar informações de maneira eficiente.
- `chromadb_web.py`: O script demonstra como extrair informações de páginas web, dividir o texto em chunks menores, e
  persistir esses dados em um banco vetorizado ChromaDB para consultas futuras.
- `qa_chromadb.py` O script demonstra como integrar a recuperação de informações armazenadas em um banco vetorizado
  ChromaDB com a geração de respostas usando o modelo de linguagem da OpenAI. Este projeto ilustra como combinar a busca
  por similaridade de documentos com a geração de texto para fornecer respostas mais informadas e contextuais.

### Por que usamos o embeddings_model ao persistir os documentos?

Usamos o embeddings_model para converter o texto dos documentos em vetores de embeddings. Esses vetores são
representações numéricas do conteúdo textual e capturam o significado semântico do texto. Ao persistir os documentos
como vetores de embeddings no ChromaDB, podemos realizar buscas por similaridade de maneira eficiente. Isso permite
encontrar rapidamente documentos que são semanticamente semelhantes à consulta de busca, mesmo que não contenham
exatamente as mesmas palavras.

### Por que dividir em chunks?

Dividir um documento em chunks é importante porque facilita o processamento e a análise do texto. Os modelos de
linguagem, como os da OpenAI, têm um limite no número de tokens que podem processar de uma vez. Dividindo o documento em
partes menores, você pode garantir que cada chunk esteja dentro desse limite, permitindo um processamento mais eficiente
e evitando a perda de informações.

----

## Créditos

O documento PDF utilizado no projeto foi obtido do site Domínio
Público: http://www.dominiopublico.gov.br/download/texto/bi000043.pdf. Todos os direitos deste documento pertencem ao
Domínio Público.

## Links Importantes

- [LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- [ChromaDB](https://www.trychroma.com/)
- [FAISS](https://faiss.ai/)

## Contribuição

Estamos abertos a contribuições para melhorar este projeto! Se você tiver sugestões, melhorias ou correções de bugs,
siga estas etapas:

1. Faça um fork do repositório.
2. Crie um branch para sua feature ou correção de bug (`git checkout -b minha-feature`).
3. Implemente suas mudanças e faça commits (`git commit -m 'Minha nova feature'`).
4. Envie suas mudanças para o branch (`git push origin minha-feature`).
5. Abra um pull request descrevendo suas alterações e por que elas devem ser mescladas.

---
Agradecemos antecipadamente por suas contribuições e por ajudar a tornar este projeto ainda melhor!

