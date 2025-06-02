from fastapi import APIRouter, Depends, HTTPException
from core.banco import get_db
from sqlalchemy.orm import Session
from typing import List
from models.cliente import Cliente as ClienteModel
from schemas.cliente import ClienteUpdate, ClienteResponse, ClienteCreate
from services import cliente_service


router = APIRouter(prefix="/clientes", tags=["Clientes"])
@router.post("/", response_model=ClienteResponse)
def criar(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.criar_cliente(db, cliente)

@router.get("/", response_model=list[ClienteResponse])
def listar(db: Session = Depends(get_db)):
    return cliente_service.listar_clientes(db)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def buscar(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.buscar_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar(cliente_id: int, dados: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = cliente_service.atualizar_cliente(db, cliente_id, dados)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.delete("/{cliente_id}")
def deletar(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.deletar_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"ok": True, "mensagem": "Cliente excluído com sucesso"}