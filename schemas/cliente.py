from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.banco import SessionLocal
from models.Cliente import Cliente

from pydantic import BaseModel

class ClienteModel(BaseModel):
    nome: str
    cnpj: str
    cpf:  str
    projeto: str
    contato: str

class ClienteCreate(ClienteModel):
    pass

class ClienteResponse(ClienteModel):
    id: int

    class Config:
       from_attributes = True
