from pydantic import BaseModel
from typing import Optional

class MaterialBase(BaseModel):
    nome: str
    unidade_medida: str
    preco: float
    quantidade: float
    fornecedor: str
    projeto_id: Optional[int] = None

class VincularMaterialProjeto(BaseModel):
    material_id: int
    projeto_id: Optional[int] = None

class MaterialCreate(MaterialBase): # CREATE: entrada de dados para criação
    pass

class MaterialResponse(MaterialBase): # RESPONSE: retornar dados ao cliente
    id: int
    class Config:
        from_attributes = True

class MaterialUpdate(BaseModel):
    nome: Optional[str]
    unidade_medida: Optional[str]
    preco: Optional[float]
    quantidade: Optional[float]
    fornecedor: Optional[str]
    projeto_id: Optional[int] = None

    class Config:
        from_attributes = True


        