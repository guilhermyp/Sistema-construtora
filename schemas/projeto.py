from pydantic import BaseModel
from typing import Optional, List
from schemas.material import MaterialResponse



class ProjetoModel(BaseModel):
    nome: str
    descricao: str
    data_inicio: str
    data_fim: str
    status: str
    custo_total: float
    custo_atual: float
    progresso: float
    funcionarios_ids: Optional[List[int]] = []


class ProjetoResponse(ProjetoModel):
    id: int

    class Config:
        from_attributes = True

class ProjetoComMateriaisResponse(ProjetoResponse):
    materiais: List[MaterialResponse]

class ProjetoCreate(ProjetoModel):
    pass

class ProjetoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    data_inicio: Optional[str] = None
    data_fim: Optional[str] = None
    status: Optional[str] = None
    custo_total: Optional[float] = None
    progresso: Optional[float] = None
    funcionarios_ids: Optional[List[int]] = []