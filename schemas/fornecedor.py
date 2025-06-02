from pydantic import BaseModel
from typing import Optional

# RESPOSTA
class FornecedorBase(BaseModel):
    cnpj: str
    nome: str
    contato: str
    tipo_material: str

class FornecedorCreate(FornecedorBase):
    pass

# PUT/PATCH
class FornecedorUpdate(BaseModel):
    cnpj: Optional[str] = None
    nome: Optional[str] = None
    contato: Optional[str] = None
    tipo_material: Optional[str] = None

# GET
class FornecedorResponse(FornecedorBase):
    id: int

    class Config:
        from_attributes = True  