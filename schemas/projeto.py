from pydantic import BaseModel
from typing import Optional


class ProjetoBase(BaseModel):
    nome: str
    descricao: str
    data_inicio: str
    data_fim: str
    status: str
    custo_total: float
    custo_atual: float
    progresso: float
    responsavel_projeto: Optional[str] = None


class ProjetoCreate(ProjetoBase):
    pass


class ProjetoResponse(ProjetoBase):
    id: int

    class Config:
        orm_mode = True
