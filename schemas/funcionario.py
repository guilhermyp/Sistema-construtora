from pydantic import BaseModel
from typing import Optional


class FuncionarioModel(BaseModel):
    nome: str
    cpf: str
    cargo: str
    salario: float
    projeto_id: Optional[int] = None


class FuncionarioCreate(FuncionarioModel):
    pass


class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    cargo: Optional[str] = None
    salario: Optional[float] = None
    projeto_id: Optional[int] = None


class FuncionarioResponse(FuncionarioModel):
    id: int

    class Config:
        from_attributes = True
