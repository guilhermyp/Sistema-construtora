from fastapi import APIRouter, Depends, HTTPException
from models import Cliente
from core.banco import get_db
from sqlalchemy.orm import Session
from typing import List
from models.cliente import Cliente
from schemas.cliente import ClienteCreate, ClienteResponse


# SCHEMA Representa dados de entrada/saída na API

# router = APIRouter(prefix="/clientes", tags=["Clientes"])

# @router.post("/", response_model=ClienteResponse)
# def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
#     db_cliente = Cliente(**cliente.dict())
#     db.add(db_cliente)
#     db.commit()
#     db.refresh(db_cliente)
#     return db_cliente

# @router.get("/", response_model=list[ClienteResponse])
# def listar_clientes(db: Session = Depends(get_db)):
#     return db.query(Cliente).all()