from pydantic import BaseModel
from typing import Optional

class Funcionario(BaseModel):
    nome: str
    cpf: str
    cargo: str
    salario: float
