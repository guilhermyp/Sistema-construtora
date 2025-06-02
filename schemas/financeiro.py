from pydantic import BaseModel
from datetime import date
from typing import Optional

class FinanceiroBase(BaseModel):
    tipo: str
    descricao: Optional[str] = None
    valor: float
    data: date
    funcionario_id: Optional[int] = None
    projeto_id: Optional[int] = None
    material_id: Optional[int] = None

class FinanceiroCreate(FinanceiroBase):
    pass

class FinanceiroUpdate(BaseModel):
    tipo: Optional[str] = None
    descricao: Optional[str] = None
    valor: Optional[float] = None
    data: Optional[date] = None
    funcionario_id: Optional[int] = None
    projeto_id: Optional[int] = None
    material_id: Optional[int] = None

class FinanceiroResponse(FinanceiroBase):
    id: int

    class Config:
        orm_mode = True
