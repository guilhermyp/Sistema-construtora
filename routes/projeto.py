
from fastapi import APIRouter
from schemas.projeto import Projeto

router = APIRouter(prefix="/projeto", tags=["Projeto"])

@router.post("/")
def criar_projeto(projeto: Projeto):
    return {"mensagem": "Projeto criado", "dados": projeto}