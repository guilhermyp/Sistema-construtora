from sqlalchemy import Column, Integer, String, Float
from core.banco import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
class Material(Base):
    __tablename__ = "materiais"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    unidade_medida = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Float, nullable=False)
    fornecedor = Column(String(100), nullable=False)
    projeto = Column(String(100), nullable=False)
    

