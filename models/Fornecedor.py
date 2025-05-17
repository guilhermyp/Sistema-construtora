from pydantic import BaseModel
from typing import Optional

class Fornecedor(BaseModel):
    cnpj: str
    nome: str
    contato: str
    tipo_material: str