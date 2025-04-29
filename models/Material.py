from pydantic import BaseModel
from typing import Optional

class Material(BaseModel):
    codigo: int
    nome: str
    unidade_medida: str
    preco: float
