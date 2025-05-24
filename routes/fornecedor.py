from fastapi import APIRouter
from schemas.fornecedor import Fornecedor

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@router.post("/")
def criar_fornecedor(fornecedor: Fornecedor):
    return {"mensagem": "Fornecedor criado", "dados": fornecedor}
