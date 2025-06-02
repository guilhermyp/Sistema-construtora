from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from core.banco import get_db  
from models.fornecedor import Fornecedor as FornecedorModel
from schemas.fornecedor import FornecedorCreate, FornecedorResponse, FornecedorUpdate
from services import fornecedor_service

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])

#CADASTRAR FONRECEDORES
@router.post("/", response_model=FornecedorResponse)
def criar(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    return fornecedor_service.criar_fornecedor(db, fornecedor)

#LISTAR FONRECEDORES
@router.get("/", response_model=list[FornecedorResponse])
def listar(db: Session = Depends(get_db)):
    return fornecedor_service.listar_fornecedores(db)

#BUSCAR POR ID
@router.get("/{fornecedor_id}", response_model=FornecedorResponse)
def buscar(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = fornecedor_service.buscar_fornecedor(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

#ATUALIZAR POR ID
@router.put("/{fornecedor_id}")
def atualizar(fornecedor_id: int, dados: FornecedorUpdate, db: Session = Depends(get_db)):
    fornecedor = fornecedor_service.atualizar_fornecedor(db, fornecedor_id, dados)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

#DELETAR POR ID
@router.delete("/{fornecedor_id}")
def deletar(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = fornecedor_service.deletar_fornecedor(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return {"ok": True, "mensagem": "Fornecedor excluído com sucesso"}