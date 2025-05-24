from pydantic import BaseModel


class FornecedorBase(BaseModel):
    cnpj: str
    nome: str
    contato: str
    tipo_material: str


class FornecedorCreate(FornecedorBase):
    pass


class FornecedorResponse(FornecedorBase):
    id: int

    class Config:
        orm_mode = True
