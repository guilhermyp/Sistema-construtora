from pydantic import BaseModel
from typing import Optional


class Financeiro(BaseModel):
    id: int
    projeto_id: int
    tipo: str  # 'receita' ou 'despesa'
    valor: float
    datetime: str
    descricao: Optional[str] = None
    status: str  # 'pago' ou 'pendente'
    forma_pagamento: Optional[str] = None  # 'dinheiro', 'cartão', 'transferencia', 'PIX'
    categoria: Optional[str] = None  # 'material','serviço','outros'
    responsavel: Optional[str] = None
    projeto: Optional[str] = None  # Nome do projeto associado
    cliente: Optional[str] = None  # Nome do cliente associado