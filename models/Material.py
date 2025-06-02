from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional
from core.banco import Base
from models.projeto import Projeto

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    unidade_medida = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Float, nullable=False)
    fornecedor = Column(String(100), nullable=False)

    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    projeto = relationship("Projeto", back_populates="materiais")