API LLM Local com FastAPI
API simples para geração de texto e análise de sentimento usando modelos gratuitos Hugging Face rodando localmente, protegida por chave de API.

Funcionalidades
Geração de texto com o modelo google/flan-t5-base

Análise de sentimento com o modelo nlptown/bert-base-multilingual-uncased-sentiment

Autenticação simples via chave API no header x-api-key

Documentação interativa via Swagger UI (/docs)

Testes unitários com pytest

Requisitos
Python 3.8+

Pacotes:

fastapi

uvicorn

python-dotenv

transformers

torch

pytest (para testes)

httpx (para testes)

Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://seurepositorio.git
cd llm_api
Instale dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Crie arquivo .env com sua chave:

env
Copiar
Editar
LOCAL_API_KEY=ceia2025
Uso
Execute a API:

bash
Copiar
Editar
uvicorn main:app --reload
Acesse a documentação interativa:

http://127.0.0.1:8000/docs
