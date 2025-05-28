from pydantic import BaseModel


class FornecedorModel(BaseModel):
    cnpj: str
    nome: str
    contato: str
    tipo_material: str


class FornecedorCreate(FornecedorModel):
    pass


class FornecedorResponse(FornecedorModel):
    id: int

    class Config:
        from_attributes = True
