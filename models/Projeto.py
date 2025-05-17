from pydantic import BaseModel
from typing import Optional

class Projeto(BaseModel):
    id: int
    nome: str
    descricao: str
    data_inicio: str
    data_fim: str
    status: str
    custo_total: float
    custo_atual: float
    progresso: float
    responsavel_projeto: Optional[str] = None


