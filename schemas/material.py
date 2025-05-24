from pydantic import BaseModel

class MaterialBase(BaseModel):
    nome: str
    unidade_medida: str
    preco: float
    quantidade: float
    fornecedor: str
    projeto: str

class MaterialCreate(MaterialBase): # CREATE: entrada de dados para criação
    pass

class MaterialResponse(MaterialBase): # RESPONSE: retornar dados ao cliente
    id: int

    class Config:
        orm_mode = True
