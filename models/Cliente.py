from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    cnpj: str
    cpf: str
    nome: str
    projeto: str
    contato: str
    