from fastapi import APIRouter
from schemas.funcionario import Funcionario

router = APIRouter(prefix="/funcionario", tags=["Funcionario"])

@router.post("/")
def criar_funcionario(funcionario: Funcionario):
    return {"mensagem": "Funcionario criado", "dados": funcionario}