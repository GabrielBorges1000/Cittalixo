from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_listar_pontos():
    response = client.get("/pontos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_criar_ponto():

    novo_ponto = {
        "nome": "Ecoponto Teste",
        "tipo": "Eletrônicos",
        "endereco": "Rua Teste",
        "latitude": -8.05,
        "longitude": -34.88
    }

    response = client.post(
        "/pontos",
        json=novo_ponto
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["nome"] == "Ecoponto Teste"