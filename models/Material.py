from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from typing import Optional
from core.banco import Base

class Material(BaseModel):
    __tablename__ = "materiais"
    id = Collumn(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    unidade_medida = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Float, nullable=False)
    fornecedor = Column(String(100), nullable=False)
    projeto = Column(String(100), nullable=False)
    

