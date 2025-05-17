from pydantic import BaseModel

class MaterialBase(BaseModel):
    nome: str
    unidade_medida: str
    preco: float
    quantidade: float
    fornecedor: str
    projeto: str

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: int

    class Config:
        orm_mode = True
