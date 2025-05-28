from pydantic import BaseModel
from typing import Optional

class Financeiro(BaseModel):
    id: int
    projeto_id: int
    tipo: str
    valor: float
    datetime: str
    descricao: Optional[str] = None
    status: str
    forma_pagamento: Optional[str] = None
    categoria: Optional[str] = None
    responsavel: Optional[str] = None
    projeto: Optional[str] = None  # associação
    cliente: Optional[str] = None  

    class Config:
        from_attributes = True  # SQLAlchemy
