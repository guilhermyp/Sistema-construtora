
from typing import Optional

from pydantic import BaseModel

class ClienteModel(BaseModel):
    nome: str
    cnpj: str
    cpf:  str
    contato: str
    projeto_id: Optional[int] = None

class ClienteCreate(ClienteModel):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    cnpj: Optional[str] = None
    cpf: Optional[str] = None
    contato: Optional[str] = None
    projeto_id: Optional[int] = None

class ProjetoSimples(BaseModel):
    id: int
    nome: str

class Config:
        from_atributes = True
class ClienteResponse(ClienteModel):
    id: int
    projeto: Optional[ProjetoSimples]
    
    class Config:
       from_attributes = True
