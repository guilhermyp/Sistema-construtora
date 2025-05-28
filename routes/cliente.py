from fastapi import APIRouter, Depends, HTTPException
from core.banco import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.cliente import ClienteCreate, ClienteResponse
from models.Cliente import Cliente as ClienteModel


router = APIRouter(prefix="/clientes", tags=["Clientes"])
@router.post("/")
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = ClienteModel(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente
