from pydantic import BaseModel
from typing import Optional


class ProjetoModel(BaseModel):
    nome: str
    descricao: str
    data_inicio: str
    data_fim: str
    status: str
    custo_total: float
    custo_atual: float
    progresso: float
    responsavel_projeto: Optional[str] = None


class ProjetoCreate(ProjetoModel):
    pass


class ProjetoResponse(ProjetoModel):
    id: int

    class Config:
        from_attributes = True
