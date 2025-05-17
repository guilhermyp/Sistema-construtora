from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from banco.conexao import SessionLocal
from models.cliente import Cliente
from schemas.cliente import ClienteCreate, ClienteResponse

from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    cnpj: str
    cpf:  str
    projeto: str
    contato: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        orm_mode = True
