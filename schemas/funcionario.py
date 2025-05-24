from pydantic import BaseModel
from typing import Optional


class FuncionarioBase(BaseModel):
    nome: str
    cpf: str
    cargo: str
    salario: float


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioResponse(FuncionarioBase):
    id: int

    class Config:
        orm_mode = True
