from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

# Definimos a chave correta para autenticação
API_KEY = os.getenv("LOCAL_API_KEY", "ceia2025")

def test_generate_valid():
    response = client.post(
        "/llm",
        headers={"x-api-key": API_KEY},
        json={"text": "Era uma vez um dragão que", "task": "generate"}
    )
    assert response.status_code == 200
    assert "result" in response.json()

def test_sentiment_valid():
    response = client.post(
        "/llm",
        headers={"x-api-key": API_KEY},
        json={"text": "Eu amei o filme!", "task": "sentiment"}
    )
    assert response.status_code == 200
    assert "result" in response.json()
    assert "Sentimento" in response.json()["result"]

def test_invalid_api_key():
    response = client.post(
        "/llm",
        headers={"x-api-key": "wrongkey"},
        json={"text": "Teste com chave errada", "task": "generate"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"

def test_invalid_task():
    response = client.post(
        "/llm",
        headers={"x-api-key": API_KEY},
        json={"text": "Teste", "task": "traduzir"}
    )
    assert response.status_code == 400
    assert "Tarefa inválida" in response.json()["detail"]
