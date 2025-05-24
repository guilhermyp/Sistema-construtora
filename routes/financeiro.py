from fastapi import APIRouter
from schemas.financeiro import Financeiro

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])

@router.post("/")
def criar_financeiro(financeiro: Financeiro):
    return {"mensagem": "Financeiro criado", "dados": financeiro}
