from pydantic import BaseModel
from typing import Optional


class FuncionarioModel(BaseModel):
    nome: str
    cpf: str
    cargo: str
    salario: float


class FuncionarioCreate(FuncionarioModel):
    pass


class FuncionarioResponse(FuncionarioModel):
    id: int

    class Config:
        from_attributes = True
