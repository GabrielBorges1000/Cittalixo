from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(
    title="CittaLixo API",
    description="API para gerenciamento de pontos de coleta de resíduos",
    version="1.0.0"
)

# Banco temporário em memória
pontos = [
    {
        "id": 1,
        "nome": "Ecoponto Centro",
        "tipo": "Recicláveis",
        "endereco": "Rua do Sol, 100",
        "latitude": -8.05428,
        "longitude": -34.8813
    }
]

# Modelo de dados
class Ponto(BaseModel):
    nome: str
    tipo: str
    endereco: str
    latitude: float
    longitude: float


# Página principal
@app.get("/")
def inicio():
    return FileResponse("index.html")


# Health Check (Observabilidade)
@app.get("/health")
def health():
    return {
        "status": "ok",
        "aplicacao": "CittaLixo"
    }


# Listar todos os pontos
@app.get("/pontos")
def listar_pontos():
    return pontos


# Buscar ponto por ID
@app.get("/pontos/{id}")
def buscar_ponto(id: int):

    for ponto in pontos:
        if ponto["id"] == id:
            return ponto

    return {"erro": "Ponto não encontrado"}


# Criar ponto
@app.post("/pontos")
def criar_ponto(ponto: Ponto):

    novo_ponto = {
        "id": len(pontos) + 1,
        "nome": ponto.nome,
        "tipo": ponto.tipo,
        "endereco": ponto.endereco,
        "latitude": ponto.latitude,
        "longitude": ponto.longitude
    }

    pontos.append(novo_ponto)

    return novo_ponto


# Atualizar ponto
@app.put("/pontos/{id}")
def atualizar_ponto(id: int, ponto_atualizado: Ponto):

    for ponto in pontos:

        if ponto["id"] == id:

            ponto["nome"] = ponto_atualizado.nome
            ponto["tipo"] = ponto_atualizado.tipo
            ponto["endereco"] = ponto_atualizado.endereco
            ponto["latitude"] = ponto_atualizado.latitude
            ponto["longitude"] = ponto_atualizado.longitude

            return ponto

    return {"erro": "Ponto não encontrado"}


# Remover ponto
@app.delete("/pontos/{id}")
def remover_ponto(id: int):

    for ponto in pontos:

        if ponto["id"] == id:
            pontos.remove(ponto)

            return {
                "mensagem": "Ponto removido com sucesso"
            }

    return {"erro": "Ponto não encontrado"}